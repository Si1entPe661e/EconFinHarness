# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `base::is.na`

Used in 687 of 1163 R papers (59%) — list("Not Available") / Missing Values.

Most common option set: none; at least one call in 687 papers (100%).

```r
  if(is.na(d)) d = 0
```
JASA 2026, [doi:10.1080/01621459.2025.2544397](https://doi.org/10.1080/01621459.2025.2544397), `code/github_richarddmorey_MoreyDavisStober_pcurveASA/R_utility/utility_density.R` line 70; license file: MIT.

### `base::unique`

Used in 553 of 1163 R papers (48%) — Extract Unique Elements.

Options (share of these 553 papers): `by` 5%, `MARGIN` 0.5%, `fromLast` 0.5%, `na.rm` 0.4%.

Most common option set: none; at least one call in 549 papers (99%).

```r
TIMES <- TBL |> pull(HD) |> unique() |> sort()
```
JASA 2026, [doi:10.1080/01621459.2025.2596288](https://doi.org/10.1080/01621459.2025.2596288), `code/figshare_30850751/figure_6.R` line 56; license file: CC0.

### `base::merge`

Used in 233 of 1163 R papers (20%) — Merge Two Data Frames.

Options (share of these 233 papers): `by` 83%, `all.x` 52%, `all` 29%, `by.x` 28%, `by.y` 27%, `all.y` 20%, `allow.cartesian` 9%, `sort` 8%, `suffixes` 7%, `x` 6%.

Most common option set: `by`; at least one call in 143 papers (61%).

```r
merged_data <- merge(Combined_sim_OC_results, Combined_DLT_res_results, by = c("scenario", "Method"))
```
JASA 2026, [doi:10.1080/01621459.2026.2624839](https://doi.org/10.1080/01621459.2026.2624839), `code/github_ShuqiWang-sw_AdaptiveStagger_reproduce/TableS1/result_agg_code_TableS1.R` line 44; license file: MIT.

Next most common option set: `all.x`, `by`; at least one call in 91 papers (39%).

```r
dff2 <- merge(dff2, averages, by = "RID", all.x = TRUE)
```
IJOC 2025, [doi:10.1287/ijoc.2023.0282](https://doi.org/10.1287/ijoc.2023.0282), `code/github_INFORMSJoC_2023.0282/scripts/Tables 7-8/real data2.R` line 34; license file: MIT.

### `dplyr::left_join`

Used in 206 of 1163 R papers (18%) — Mutating joins.

Options (share of these 206 papers): `by` 82%, `suffix` 8%, `y` 4%, `relationship` 3%, `x` 3%, `multiple` 2%.

Most common option set: `by`; at least one call in 164 papers (80%).

```r
  left_join(hkm_m, by = "ym")
```
ReStud 2026, [doi:10.1093/restud/rdag085](https://doi.org/10.1093/restud/rdag085), `code/zenodo_20598953/ReplicationPackageRestud_v2/ReplicationPackageRestud/code/table1.R` line 147; license file: MIT.

Next most common option set: none; at least one call in 90 papers (44%).

```r
  tm_mu <- left_join(df_x, tm_mu)
```
JASA 2026, [doi:10.1080/01621459.2026.2661377](https://doi.org/10.1080/01621459.2026.2661377), `code/figshare_32125854/reproducibility_repo/seqdx_jasa_repo-public/seqDxDev/simu/by_math/simu_by_math_prepare.R` line 138; license file: GPL.

### `stats::na.omit`

Used in 153 of 1163 R papers (13%) — Handle Missing Values in Objects.

Options (share of these 153 papers): `cols` 5%.

Most common option set: none; at least one call in 152 papers (99%).

```r
    kd.qs <- density(na.omit(qs))
```
JASA 2026, [doi:10.1080/01621459.2026.2721401](https://doi.org/10.1080/01621459.2026.2721401), `code/github_lmhagar_SeqDesign/06_ex2_functions.R` line 157; license file: MIT.

### `base::stopifnot`

Used in 120 of 1163 R papers (10%) — Ensure the Truth of R Expressions.

Most common option set: none; at least one call in 119 papers (99%).

```r
stopifnot(length(date_range) == nrow(dat_all))
```
JASA 2026, [doi:10.1080/01621459.2026.2621515](https://doi.org/10.1080/01621459.2026.2621515), `code/github_XiaoyuMa94_Conditional-XVAE/FWI Data Analysis/data_preparation.R` line 116; license file: MIT.

### `base::duplicated`

Used in 117 of 1163 R papers (10%) — Determine Duplicate Elements.

Options (share of these 117 papers): `fromLast` 10%, `by` 4%, `MARGIN` 2%.

Most common option set: none; at least one call in 111 papers (95%).

```r
  iIncidentStart    <- which(!duplicated(d$id))-1 # -1 for C++
```
JASA 2026, [doi:10.1080/01621459.2025.2597050](https://doi.org/10.1080/01621459.2025.2597050), `code/github_gregridgeway_COS-police-use-of-force/code/mcmcConditionalStereotype.R` line 20; license file: MIT.

### `dplyr::distinct`

Used in 96 of 1163 R papers (8%) — Keep distinct/unique rows.

Options (share of these 96 papers): `.keep_all` 40%.

Most common option set: none; at least one call in 86 papers (90%).

```r
  temp %>% distinct() %>%
```
JASA 2026, [doi:10.1080/01621459.2025.2547968](https://doi.org/10.1080/01621459.2025.2547968), `code/figshare_29950540/Code/Code/Reproduce/lib/additive_summary_plot_2.R` line 16; license file: GPL.

Next most common option set: `.keep_all`; at least one call in 38 papers (40%).

```r
master_s1 <- master_s1 %>% distinct(sid, dmatch, study, randomized_date, .keep_all=T) %>% mutate(blocknum = factor(blocknum))
```
AER 2023, [doi:10.1257/aer.20210434](https://doi.org/10.1257/aer.20210434), `code/scripts_r/data_scripts/building_eleventh_grade_outcomes.R` line 10; license file: BSD.
