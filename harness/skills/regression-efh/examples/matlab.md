# MATLAB examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1084 MATLAB replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `regress`

Used in 113 of 1084 MATLAB papers (10%) — Multiple linear regression.

Most common option set: none; at least one call in 113 papers (100%).

```matlab
b_1 = regress(ly_1,X_1); %Women
```
JPE 2024, [doi:10.1086/732532](https://doi.org/10.1086/732532), `code/dataverse_LBH9ND/Replication_JPE_Internal_estimation_Inputs/moments.m` line 458; license file: BSD.

### `fitlm`

Used in 52 of 1084 MATLAB papers (5%) — Fit linear regression model.

Options (share of these 52 papers): `Intercept` 27%, `Weights` 10%.

Most common option set: none; at least one call in 40 papers (77%).

```matlab
    mdl = fitlm(montD_fe,dateD_fe);
```
QJE 2025, [doi:10.1093/qje/qjaf018](https://doi.org/10.1093/qje/qjaf018), `code/dataverse_JWCHRZ/analysis_cluster_code/Replicate.m` line 121; license file: MIT.

Next most common option set: `Intercept`; at least one call in 14 papers (27%).

```matlab
    dlm=fitlm(RandD_sales(1:end-1,kkkkk),RandD_sales(2:end,kkkkk),'Intercept',false);
```
ReStud 2024, [doi:10.1093/restud/rdad041](https://doi.org/10.1093/restud/rdad041), `code/zenodo_7617222/replication_package_v2/replication_package_v2/Replication_Package_for_Model/Codes/Model_Simulation.m` line 271; license file: MIT.

### `glmfit`

Used in 23 of 1084 MATLAB papers (2%) — Fit generalized linear regression model.

Options (share of these 23 papers): `Link` 65%, `Constant` 39%, `Weights` 9%.

Most common option set: `Link`; at least one call in 7 papers (30%).

```matlab
reg_bank_credit_predicting_crash = glmfit(bank_credit_ratio_sim,  equity_crash_next_year,'binomial','Link','probit');
```
JPE 2025, [doi:10.1086/733423](https://doi.org/10.1086/733423), `code/dataverse_TIL7KK/Model_Codes_Model/simulation_moments.m` line 404; license file: BSD.

Next most common option set: none; at least one call in 6 papers (26%).

```matlab
b = glmfit(pred_pc(SubId == 0), Y(SubId == 0), 'normal');
```
JASA 2023, [doi:10.1080/01621459.2022.2102984](https://doi.org/10.1080/01621459.2022.2102984), `code/github_wuyx5_LESA/Code and Example Data/PACE_matlab-master/release2.17/examples/exampleStringing.m` line 41; license file: BSD.

### `poissrnd`

Used in 22 of 1084 MATLAB papers (2%) — Random numbers from Poisson distribution.

Most common option set: none; at least one call in 22 papers (100%).

```matlab
            bid_count = poissrnd( obj.lambda, size(obj.plant,1), 1 );
```
QJE 2025, [doi:10.1093/qje/qjaf009](https://doi.org/10.1093/qje/qjaf009), `code/dataverse_PDFDKR/AnonymizedETSReplication_01Code_model_matlab_.etsModel/etsModel.m` line 152; license file: BSD.

### `lasso`

Used in 9 of 1084 MATLAB papers (0.8%) — Lasso or elastic net regularization for linear models.

Options (share of these 9 papers): `CV` 56%, `Lambda` 44%, `NumLambda` 44%, `Alpha` 33%, `DFmax` 22%, `Options` 22%.

Most common option set: `Lambda`; at least one call in 2 papers (22%).

```matlab
[Profits_LASSO_optimal,Profits_LASSO_optimal_FitInfo] = lasso(Xinitial(sample_val_fn_approx>0,:),profits_static(sample_val_fn_approx>0,:),...
'Lambda',rate_lasso);
```
ReStud 2025, [doi:10.1093/restud/rdaf011](https://doi.org/10.1093/restud/rdaf011), `code/zenodo_14083198/Replication_BKZ_2024_v2/code/4_dynamics/NE70_Dynamic_Estimation_Splines_S90b.m` lines 1632-1633.

### `mvregress`

Used in 6 of 1084 MATLAB papers (0.6%) — Multivariate linear regression.

Options (share of these 6 papers): `algorithm` 33%.

Most common option set: none; at least one call in 4 papers (67%).

```matlab
    beta_rr = mvregress(DesignX(idx,:),Y(idx));
```
JFE 2025, [doi:10.1016/j.jfineco.2025.104010](https://doi.org/10.1016/j.jfineco.2025.104010), `code/mendeley_925crksynw_v2/matlab/figure_cumulative_return.m` line 163.

Next most common option set: `algorithm`; at least one call in 2 papers (33%).

```matlab
[Be,~] = mvregress(X,Ye,'algorithm','cwls');
```
JFE 2025, [doi:10.1016/j.jfineco.2025.104059](https://doi.org/10.1016/j.jfineco.2025.104059), `code/mendeley_kgdzjdksrb_v2/Replication_code/Replication code/constructCFDR_fullvar.m` line 29.
