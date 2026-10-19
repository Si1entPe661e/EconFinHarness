# MATLAB examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1084 MATLAB replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `plot`

Used in 724 of 1084 MATLAB papers (67%) — 2-D line plot.

Options (share of these 724 papers): `LineWidth` 78%, `Color` 50%, `MarkerSize` 29%, `LineStyle` 24%, `MarkerFaceColor` 13%, `Marker` 9%, `MarkerEdgeColor` 6%, `DisplayName?` 4%, `Parent?` 2%, `HandleVisibility?` 2%.

Most common option set: `LineWidth`; at least one call in 427 papers (59%).

```matlab
    h3 = plot(x1,x_H,'-k','LineWidth',3);
```
MPC 2026, [doi:10.1007/s12532-026-00306-5](https://doi.org/10.1007/s12532-026-00306-5), `code/github_Wu-Can_ALM-SNCG-SMM/Test0_figures_1_2/Figure1_SM_ASM.m` line 77; license file: GPL.

Next most common option set: none; at least one call in 410 papers (57%).

```matlab
        plot(x,Y)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0048](https://doi.org/10.1287/ijoc.2023.0048), `code/github_INFORMSJoC_2023.0048/scripts/NumericalAnalysis_resourceAllocation.m` line 228; license file: MIT.

### `figure`

Used in 690 of 1084 MATLAB papers (64%) — Create figure window.

Options (share of these 690 papers): `Position` 16%, `Name` 9%, `Units` 6%, `Color` 6%, `visible?` 6%, `NumberTitle?` 4%, `outerposition?` 2%, `Renderer?` 2%, `DefaultAxesFontSize?` 1%, `PaperPosition?` 1%.

Most common option set: none; at least one call in 600 papers (87%).

```matlab
figure;
```
IJOC 2026, [doi:10.1287/ijoc.2023.0465](https://doi.org/10.1287/ijoc.2023.0465), `code/github_INFORMSJoC_2023.0465/scripts/draw_feasible_region.m` line 95; license file: MIT.

### `hold`

Used in 658 of 1084 MATLAB papers (61%) — Retain current plot when adding new plots.

Most common option set: none; at least one call in 658 papers (100%).

```matlab
hold on
```
IJOC 2026, [doi:10.1287/ijoc.2025.1169](https://doi.org/10.1287/ijoc.2025.1169), `code/github_INFORMSJoC_2025.1169/scripts/run_RMSE_iterations.m` line 36; license file: MIT.

### `gca`

Used in 546 of 1084 MATLAB papers (50%) — Current axes or chart.

Most common option set: none; at least one call in 546 papers (100%).

```matlab
if (nargin == 0), fig_hndl = gcf; axes_hndl = gca; end;
```
IJOC 2026, [doi:10.1287/ijoc.2025.1183](https://doi.org/10.1287/ijoc.2025.1183), `code/github_INFORMSJoC_2025.1183/scripts/q_tools/magnify.m` line 122; license file: MIT.

### `close`

Used in 541 of 1084 MATLAB papers (50%) — Close one or more figures.

Most common option set: none; at least one call in 541 papers (100%).

```matlab
    close all
```
JPE 2026, [doi:10.1086/741623](https://doi.org/10.1086/741623), `code/dataverse_RWAODQ/run_mc_R01_DGP01.m` line 242; license file: MIT.

### `gcf`

Used in 411 of 1084 MATLAB papers (38%) — Current figure handle.

Most common option set: none; at least one call in 411 papers (100%).

```matlab
set(gcf,'unit','points','PaperUnits','points','PaperPosition',[0,0,width,width/5],...
```
JRSSB 2026, [doi:10.1093/jrsssb/qkag020](https://doi.org/10.1093/jrsssb/qkag020), `code/github_SongWei-GT_online_kernel_cusum/example1_stat_traj.m` line 93; license file: MIT.

### `print`

Used in 297 of 1084 MATLAB papers (27%) — Print figure or save to specific file format.

Options (share of these 297 papers): `Figure_3?` 1%, `Figure3?` 1%, `figure_1?` 1%, `figure_2?` 1%, `Figure2?` 0.7%, `Figure4?` 0.7%, `Figure5?` 0.7%, `Figure6?` 0.7%, `Figure_F1?` 0.7%, `Figure_F2?` 0.7%.

Most common option set: none; at least one call in 280 papers (94%).

```matlab
print(fig,'figures/damp_vs_full.pdf','-dpdf');
```
MPC 2026, [doi:10.1007/s12532-025-00302-1](https://doi.org/10.1007/s12532-025-00302-1), `code/github_RPI-OPT_DampedALM/LCQP/test_damp_vs_full.m` line 99; license file: MIT.

### `saveas`

Used in 239 of 1084 MATLAB papers (22%) — Save figure to specific file format.

Options (share of these 239 papers): `Figure2?` 0.8%, `Figure3a?` 0.8%, `Figure3b?` 0.8%, `Figure5a?` 0.8%, `Figure5b?` 0.8%, `Figure6a?` 0.8%, `Figure6b?` 0.8%, `figure4?` 0.8%.

Most common option set: none; at least one call in 221 papers (92%).

```matlab
saveas(fig, save_name);
```
IJOC 2026, [doi:10.1287/ijoc.2024.0914](https://doi.org/10.1287/ijoc.2024.0914), `code/github_INFORMSJoC_2024.0914/scripts/plot_k.m` line 33; license file: MIT.
