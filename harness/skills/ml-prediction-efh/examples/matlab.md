# MATLAB examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1084 MATLAB replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `cvpartition`

Used in 10 of 1084 MATLAB papers (0.9%) — Partition data for cross-validation.

Options (share of these 10 papers): `KFold?` 60%, `HoldOut?` 30%.

Most common option set: `KFold?`; at least one call in 6 papers (60%).

```matlab
KPart = cvpartition(n,"KFold",KF);  % Set up partition for cross validation 
```
Econometrica 2026, [doi:10.3982/ecta23174](https://doi.org/10.3982/ecta23174), `code/zenodo_19442141/Replication_Package/programs/FunctionalsTypeProb.m` line 28.

Next most common option set: `HoldOut?`; at least one call in 3 papers (30%).

```matlab
	cvp = cvpartition(numDocuments, 'HoldOut', 0.1);
```
RFS 2026, [doi:10.1093/rfs/hhag021](https://doi.org/10.1093/rfs/hhag021), `code/dataverse_33PACY/RFS Code Sharing_02122026/RFS Code Sharing_02122026/Raw Data Processing/TCI and Degree Raw Data Processing.m` line 128.

### `lasso`

Used in 9 of 1084 MATLAB papers (0.8%) — Lasso or elastic net regularization for linear models.

Options (share of these 9 papers): `CV` 56%, `Lambda` 44%, `NumLambda` 44%, `Alpha` 33%, `DFmax` 22%, `Options` 22%.

Most common option set: `Lambda`; at least one call in 2 papers (22%).

```matlab
[Profits_LASSO_optimal,Profits_LASSO_optimal_FitInfo] = lasso(Xinitial(sample_val_fn_approx>0,:),profits_static(sample_val_fn_approx>0,:),...
'Lambda',rate_lasso);
```
ReStud 2025, [doi:10.1093/restud/rdaf011](https://doi.org/10.1093/restud/rdaf011), `code/zenodo_14083198/Replication_BKZ_2024_v2/code/4_dynamics/NE70_Dynamic_Estimation_Splines_S90b.m` lines 1632-1633.

### `perfcurve`

Used in 5 of 1084 MATLAB papers (0.5%) — Receiver operating characteristic (ROC) curve or other performance curve for classifier output.

Most common option set: none; at least one call in 5 papers (100%).

```matlab
[FPR,TPR,T, AUC] = perfcurve(Label,RNet,1);
```
JASA 2026, [doi:10.1080/01621459.2026.2697050](https://doi.org/10.1080/01621459.2026.2697050), `code/github_zhangheng37_ML-ODE/function/performance.m` line 6.

Next most common option set: `Alpha`, `NBoot`; at least one call in 1 paper (20%).

```matlab
    [X,Y,~,AUROC] = perfcurve(is_dstc,lpi,'yes','NBoot',NBoot,'Alpha',0.01/2);
```
JFE 2024, [doi:10.1016/j.jfineco.2024.103838](https://doi.org/10.1016/j.jfineco.2024.103838), `code/mendeley_4h62p9tdfx_v2/mp_replication_package/matlab/functions/mp_auroc.m` line 9.
