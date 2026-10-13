# DID command examples

Load the required packages and prepare the variables described beside each call. Choose the sample, comparison group, weights and inference settings for the current research design.

## R

### 1. Fixed-effects DID with lfe

Input: data frame `d` with `allunits`, `Before`, `After`, `Chain`, `BUYER_ZIP`, and `Date`. The four formula parts specify regressors, fixed effects, the empty IV part, and the cluster variable.

```r
library(lfe)
fe3 = felm(allunits~Before+After+Chain|as.factor(BUYER_ZIP)+as.factor(Date)|0|BUYER_ZIP, data=d)
summary(fe3)
```

### 2. TWFE and Sun-Abraham event studies with fixest

Input: `df` with the listed outcomes, `provider`, `year`, `treat`, `year_to_treat`, and `year_treated`. For never-treated units, use `treat = 0`, `year_to_treat = -1000`, and `year_treated = 10000`. The reference period is -1; both calls cluster by provider. Pass calendar adoption year and calendar year to `sunab`.

```r
library(fixest)
outcomes = c("share_adrd", "admissions_los", "admissions_los180", "admissions_ld")
twfe = feols(
    c(.[, outcomes]) ~ i(year_to_treat, treat, ref=c(-1, -1000)) |
    provider + year,
    data = df,
    cluster = ~provider
)
sa = feols(
    c(.[, outcomes]) ~ sunab(year_treated, year) | provider + year,
    data = df,
    cluster = ~provider
)
```

### 3. Group-time ATTs and aggregation with did

Input: `cleandat` with numeric unit identifier `uniqueid`, calendar `year`, cohort `foundationCS` (0 for never treated), cluster `cddaid`, outcome `greenness`, and the listed covariates. Choose `control_group`, `est_method`, bootstrap and confidence-band settings for the current design. Supplying `clustervars` with `bstrap = FALSE` requires checking the installed package's inference behavior.

```r
library(did)
fml = '~g0+elevation+gsl0+rain+hdd+gsl'
example_attgt <- att_gt(
    yname = "greenness",
    tname = "year",
    idname = "uniqueid",
    gname = "foundationCS",
    xformla = as.formula(fml),
    base_period = 'universal',
    clustervars = c("uniqueid", 'cddaid'),
    data = cleandat,
    cband = FALSE,
    bstrap = FALSE
)
agg.es <- aggte(example_attgt, type = "dynamic", na.rm = TRUE,
                cband = FALSE, bstrap = FALSE)
agg.simple <- aggte(example_attgt, type = "simple", na.rm = TRUE,
                    cband = FALSE, bstrap = FALSE)
agg.grp <- aggte(example_attgt, type = "group", na.rm = TRUE,
                 cband = FALSE, bstrap = FALSE)
summary(agg.es)
```

### 4. Synthetic DID with synthdid

Input: package example panel `california_prop99`, if available. This `panel.matrices` interface requires a balanced panel and simultaneous treatment adoption. `N0` counts control units and `T0` counts pre-treatment periods. The example uses placebo inference for a single treated unit.

```r
library(synthdid)
data('california_prop99')
setup = panel.matrices(california_prop99)
tau.hat = synthdid_estimate(setup$Y, setup$N0, setup$T0)
se = sqrt(vcov(tau.hat, method='placebo'))
sprintf('95%% CI (%1.2f, %1.2f)', tau.hat - 1.96 * se, tau.hat + 1.96 * se)
```

### 5. Goodman-Bacon decomposition in R

Input: `death_data` with outcome `ln_imr_pub`, absorbing treatment indicator `treated`, unit `fips`, and calendar `year`.

```r
bacon_formula <- as.formula("ln_imr_pub ~ treated")
bacon_out <- bacondecomp::bacon(
    bacon_formula,
    data = death_data,
    id_var = "fips",
    time_var = "year"
)
```

## Stata

### 6. TWFE and Sun-Abraham event studies

Input: panel with outcome `allunits`, cohort `After_f`, `After_firststata`, relative month `Event`, identifiers `dea1`, `Date`, `Datestata`, and cluster `BUYER_ZIP`. The code constructs leads and lags and omits month -1. `lastcohort` marks never-treated units. The two calls use their respective calendar-time identifiers.

```stata
replace After_f = . if After_f == 0
gen gvar = cond(After_f == ., 0, After_f)
gen lastcohort = gvar == 0
replace Event = . if After_firststata == .
forvalues l = 0/11 {
    gen L`l'event = Event == `l'
}
forvalues l = 12(-1)1 {
    gen F`l'event = Event == -`l'
}
drop F1event
gen base = 1
reghdfe allunits F*event base L*event, absorb(dea1 Date) cluster(BUYER_ZIP)
eventstudyinteract allunits F*event L*event, vce(cluster BUYER_ZIP) ///
    absorb(dea1 Datestata) cohort(After_f) control_cohort(lastcohort)
```

### 7. Weighted csdid and event aggregation

Input: county-year panel with outcome `i_tot_beds_aha_pc`, weight `births_pub`, unit `fips`, calendar `year`, and first treatment year `time_treated`. The code assigns never-treated cohorts 0 in `time_treated_2`. Choose estimator, comparison and clustering options for the current design.

```stata
gen time_treated_2 = time_treated
replace time_treated_2 = 0 if missing(time_treated)
csdid i_tot_beds_aha_pc [iw = births_pub], ///
    ivar(fips) time(year) gvar(time_treated_2) agg(event)
csdid_estat event
```

### 8. Imputation DID: static and dynamic effects

For static effects, provide a firm-year panel with `trade`, `bvd_id`, `year`, first treatment year `Ei` (missing for never-treated units), `country_num`, and bank cluster `BankID_num`. For dynamic effects, provide the country-month variables in the second call. `pretrends(18)` is the correct option spelling. Choose the horizon window and `shift(1)` for the treatment timing convention; `autosample` can change the estimation sample.

```stata
did_imputation trade bvd_id year Ei, ///
    fe(bvd_id year year#country_num) ///
    autosample cluster(BankID_num) tol(0.1)
```

```stata
global Tradecontrols "Source_exports_CHN_share Source_imports_CHN_share ln_Source_exports_CHN ln_Source_imports_CHN"
global PolicyControls "ChinaInvest_pc ChinaInvest_cum_pc AIIB FTA UNCHINA_diff"
global NeighbourControls "CNYex300yes_close"
did_imputation Source_CNYex300yes sourcecountry t first_swap if em_tag==1, ///
    fe(t sourcecountry) minn(0) autosample cluster(sourcecountry) ///
    hor(0/24) pretrends(18) ///
    controls($Tradecontrols $PolicyControls $NeighbourControls clearingbanks) ///
    maxit(1000) shift(1)
```

### 9. Legacy did_multiplegt

Input: CPS panel with outcome `employed`, state `State`, calendar `year`, binary treatment path `treat`, and weight `wtfinl`. This call uses the legacy interface. Check `did_multiplegt_old` when using newer packages; `did_multiplegt_dyn` uses different arguments. Choose the number of bootstrap replications for the current inference plan.

```stata
did_multiplegt employed State year treat, ///
    jointtestplacebo average_effect covariances robust_dynamic ///
    dynamic(6) placebo(4) breps(100) seed(515) ///
    weight(wtfinl) cluster(State)
```

### 10. Nonlinear jwdid with PPML

Input: firm-year panel with `exportrevenue`, `large`, `bvd_id`, `year`, `first_treat`, `country_num`, and `BankID`. Code `first_treat` as 0 for never-treated units. `method(ppmlhdfe)` specifies a nonlinear model and changes interpretation relative to linear DID.

```stata
jwdid exportrevenue i.large, ivar(bvd_id) tvar(year) gvar(first_treat) ///
    method(ppmlhdfe) fevar(i.country_num#i.year) cluster(BankID)
estat simple, post
```

### 11. Goodman-Bacon decomposition in Stata

Input: balanced county-year panel with `ln_imr_pub`, `treated`, `fips`, and `year`. Declare the panel before the decomposition.

```stata
xtset fips year
xtreg ln_imr_pub treated i.year, fe vce(cluster fips)
bacondecomp ln_imr_pub treated, ddetail stub(bacon_)
```

### 12. HonestDiD sensitivity calculation

Input: hospital panel with `bed_utl_rate`, event indicators `str_test_ind_b3` through `str_test_ind_p4`, and controls `log_bedday` and `cash_ta`. `pre(1 2 3)` and `post(4)` refer to coefficient positions: check their order in `e(b)` and `e(V)`. The Stata variable range depends on the data's variable order. `delta(sd)` specifies a smoothness restriction.

```stata
tsset hos_id year
quietly reghdfe bed_utl_rate str_test_ind_b3 - str_test_ind_p4 ///
    L.log_bedday L.cash_ta if year >= 2010 & year <= 2016, ///
    absorb(hos_id year) cluster(hos_id)
local upper = _se[str_test_ind_p1]
local delta = 0.25 * _se[str_test_ind_p1]
honestdid, pre(1 2 3) post(4) mvec(0(`delta')`upper') delta(sd)
```

## Python

### 13. DID with linearmodels.PanelOLS

Input: `did_df` with `pool_address`, datetime `date`, outcome `log_liquidity`, binary `treatment`, and binary `post`. The unit and time fixed effects absorb the treatment and post indicators; `treat_post` supplies the DID coefficient. The call clusters by pool.

```python
from linearmodels.panel import PanelOLS
import statsmodels.api as sm

did_df['treat_post'] = did_df['treatment'] * did_df['post']
df = did_df.set_index(['pool_address', 'date'])
y = df['log_liquidity']
X = sm.add_constant(df[['treat_post', 'treatment', 'post']])
model = PanelOLS(y, X, entity_effects=True, time_effects=True, drop_absorbed=True)
result = model.fit(cov_type='clustered', cluster_entity=True)
print(result.summary)
```
