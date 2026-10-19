# R examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1163 R replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `ggplot2::aes`

Used in 612 of 1163 R papers (53%) — Construct aesthetic mappings.

Options (share of these 612 papers): `x` 96%, `y` 94%, `color` 61%, `fill` 55%, `ymin` 42%, `ymax` 42%, `group` 39%, `linetype` 34%, `shape` 31%, `label` 24%.

Most common option set: `x`, `y`; at least one call in 380 papers (62%).

```r
    ggplot(aes(x=HD, y=U)) +
```
JASA 2026, [doi:10.1080/01621459.2025.2596288](https://doi.org/10.1080/01621459.2025.2596288), `code/figshare_30850751/figure_6.R` line 165; license file: CC0.

Next most common option set: `fill`, `x`, `y`; at least one call in 177 papers (29%).

```r
ggplot(data, aes(x = h, y = EE, fill = Method)) +
```
JASA 2026, [doi:10.1080/01621459.2025.2555057](https://doi.org/10.1080/01621459.2025.2555057), `code/github_ishspsy_transfer_learning/Code_example/Figures_code.R` line 18; license file: MIT.

### `ggplot2::ggplot`

Used in 605 of 1163 R papers (52%) — Create a new ggplot.

Options (share of these 605 papers): `data` 34%, `mapping` 6%, `fill` 0.8%, `color` 0.7%, `group` 0.3%, `show.legend` 0.3%.

Most common option set: none; at least one call in 541 papers (89%).

```r
    ggplot() + geom_hline(yintercept = 0) +
```
JASA 2026, [doi:10.1080/01621459.2025.2547968](https://doi.org/10.1080/01621459.2025.2547968), `code/figshare_29950540/Code/Code/Reproduce/lib/additive_summary_plot_2.R` line 17; license file: GPL.

Next most common option set: `data`; at least one call in 188 papers (31%).

```r
p <- ggplot(data = df) +
```
IJOC 2026, [doi:10.1287/ijoc.2023.0245](https://doi.org/10.1287/ijoc.2023.0245), `code/github_INFORMSJoC_2023.0245/scripts/Figure 8.R` line 44; license file: MIT.

### `ggplot2::theme`

Used in 566 of 1163 R papers (49%) — Modify components of a theme.

Options (share of these 566 papers): `legend.position` 80%, `legend.title` 49%, `axis.text.x` 48%, `legend.text` 41%, `plot.title` 39%, `axis.title.x` 35%, `axis.text.y` 33%, `axis.title.y` 33%, `axis.text` 32%, `panel.grid.minor` 28%.

Most common option set: `legend.position`; at least one call in 226 papers (40%).

```r
             theme(legend.position="none") +
```
JASA 2026, [doi:10.1080/01621459.2026.2721401](https://doi.org/10.1080/01621459.2026.2721401), `code/github_lmhagar_SeqDesign/02_dynamic_results.R` line 817; license file: MIT.

### `ggplot2::element_text`

Used in 471 of 1163 R papers (40%) — Theme elements.

Options (share of these 471 papers): `size` 86%, `hjust` 57%, `angle` 35%, `face` 30%, `vjust` 24%, `family` 12%, `color` 12%, `margin` 11%, `colour` 7%, `lineheight` 1%.

Most common option set: `size`; at least one call in 353 papers (75%).

```r
    axis.title.x.top = element_text(size=8),
```
JASA 2026, [doi:10.1080/01621459.2025.2544397](https://doi.org/10.1080/01621459.2025.2544397), `code/github_richarddmorey_MoreyDavisStober_pcurveASA/text/sections/04b_inadmissibility.Rmd` line 81; license file: MIT.

Next most common option set: `hjust`; at least one call in 103 papers (22%).

```r
  theme(plot.title=element_text(hjust=0.5))+
```
IJOC 2026, [doi:10.1287/ijoc.2024.0796](https://doi.org/10.1287/ijoc.2024.0796), `code/github_INFORMSJoC_2024.0796/scripts/Figure-2_code.R` line 512; license file: MIT.

### `ggplot2::geom_point`

Used in 436 of 1163 R papers (37%) — Points.

Options (share of these 436 papers): `size` 70%, `data` 31%, `shape` 25%, `color` 25%, `alpha` 22%, `position` 13%, `colour` 10%, `stroke` 7%, `fill` 7%, `mapping` 5%.

Most common option set: none; at least one call in 199 papers (46%).

```r
  geom_point() + 
```
JASA 2026, [doi:10.1080/01621459.2026.2624839](https://doi.org/10.1080/01621459.2026.2624839), `code/github_ShuqiWang-sw_AdaptiveStagger_reproduce/Figure1/Figure1_illustration of efficacy decay.R` line 14; license file: MIT.

Next most common option set: `size`; at least one call in 179 papers (41%).

```r
  geom_point(size = 3) +
```
JASA 2026, [doi:10.1080/01621459.2025.2529602](https://doi.org/10.1080/01621459.2025.2529602), `code/github_chenxuan-he_GoFHD2/plot_codes/model1_plot.R` line 13; license file: MIT.

### `ggplot2::labs`

Used in 409 of 1163 R papers (35%) — Modify axis, legend, and plot labels.

Options (share of these 409 papers): `x` 86%, `y` 84%, `title` 44%, `color` 32%, `fill` 26%, `linetype` 12%, `shape` 11%, `colour` 9%, `subtitle` 8%, `caption` 6%.

Most common option set: `x`, `y`; at least one call in 228 papers (56%).

```r
    labs(y = 'False positive rate', x = 'Cost') +
```
JASA 2026, [doi:10.1080/01621459.2026.2661377](https://doi.org/10.1080/01621459.2026.2661377), `code/figshare_32125854/reproducibility_repo/seqdx_jasa_repo-public/seqDxDev/pMRI/see_pMRI_3step.R` line 420; license file: GPL.

Next most common option set: `title`, `x`, `y`; at least one call in 113 papers (28%).

```r
  labs(x = "", y = "", title = "") +
```
JASA 2026, [doi:10.1080/01621459.2026.2625441](https://doi.org/10.1080/01621459.2026.2625441), `code/github_Jianbin-Tan_Functional-Singular-Value-Decompostion/Data_analysis_EHR.R` line 176; license file: MIT.

### `ggplot2::geom_line`

Used in 404 of 1163 R papers (35%) — Connect observations.

Options (share of these 404 papers): `size` 38%, `linewidth` 24%, `color` 23%, `data` 23%, `linetype` 20%, `alpha` 12%, `colour` 6%, `lwd` 5%, `mapping` 4%, `col` 4%.

Most common option set: none; at least one call in 234 papers (58%).

```r
  geom_line() +
```
IJOC 2026, [doi:10.1287/ijoc.2024.0691](https://doi.org/10.1287/ijoc.2024.0691), `code/github_INFORMSJoC_2024.0691/scripts/get-line.R` line 24; license file: MIT.

Next most common option set: `size`; at least one call in 111 papers (27%).

```r
    geom_line(size = 0.5) +
```
JASA 2026, [doi:10.1080/01621459.2026.2649585](https://doi.org/10.1080/01621459.2026.2649585), `code/github_TARPS-group_split-predictive-checks/spc/evaluation.R` line 175; license file: MIT.

### `ggplot2::element_blank`

Used in 380 of 1163 R papers (33%) — Theme elements.

Most common option set: none; at least one call in 380 papers (100%).

```r
  theme_bw() + theme(legend.position="top", panel.spacing.x=unit(0, "lines"), strip.text.x = element_blank())
```
IJOC 2026, [doi:10.1287/ijoc.2024.0866](https://doi.org/10.1287/ijoc.2024.0866), `code/github_INFORMSJoC_2024.0866/scripts/table2.R` line 19; license file: MIT.
