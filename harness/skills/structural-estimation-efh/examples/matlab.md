# MATLAB examples from published replication packages

Commands and functions related to this skill, as written in the author code of 1084 MATLAB replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `optimset`

Used in 334 of 1084 MATLAB papers (31%) — Create or modify optimization options structure.

Options (share of these 334 papers): `Display` 80%, `MaxIter` 62%, `MaxFunEvals` 61%, `TolFun` 61%, `TolX` 59%, `Algorithm?` 19%, `GradObj?` 12%, `LargeScale?` 10%, `TolCon?` 7%, `Hessian?` 5%.

Most common option set: `Display`; at least one call in 87 papers (26%).

```matlab
opt_solver = optimset('Display','on');
```
JPE 2025, [doi:10.1086/733423](https://doi.org/10.1086/733423), `code/dataverse_TIL7KK/Model_Codes_Model/irf_rational_and_behavioral_lvg_and_cs.m` line 22; license file: BSD.

Next most common option set: `Display`, `MaxFunEvals`, `MaxIter`, `TolFun`, `TolX`; at least one call in 57 papers (17%).

```matlab
problem.options = optimset('Display','none', 'MaxFunEvals',15000,'MaxIter',3000, 'TolFun', 1e-3, 'TolX',1e-3 );  
```
JPE 2024, [doi:10.1086/732532](https://doi.org/10.1086/732532), `code/dataverse_LBH9ND/Replication_JPE_Data/inputs_mcd.m` line 133; license file: BSD.

### `optimoptions`

Used in 229 of 1084 MATLAB papers (21%) — Create optimization options.

Options (share of these 229 papers): `Display?` 83%, `Algorithm?` 37%, `MaxIterations?` 28%, `MaxFunctionEvaluations?` 26%, `TolFun?` 26%, `FunctionTolerance?` 25%, `StepTolerance?` 24%, `OptimalityTolerance?` 21%, `MaxIter?` 20%, `MaxFunEvals?` 19%.

Most common option set: `Display?`; at least one call in 67 papers (29%).

```matlab
        options = optimoptions('fmincon', 'Display', 'off');
```
IJOC 2026, [doi:10.1287/ijoc.2023.0465](https://doi.org/10.1287/ijoc.2023.0465), `code/github_INFORMSJoC_2023.0465/scripts/Robustness_run.m` line 249; license file: MIT.

### `fsolve`

Used in 205 of 1084 MATLAB papers (19%) — Solve system of nonlinear equations.

Most common option set: none; at least one call in 205 papers (100%).

```matlab
    [x,~,exitflag] = fsolve(@(x) ahomof(x), x1,opt1);
```
IJOC 2025, [doi:10.1287/ijoc.2024.0546](https://doi.org/10.1287/ijoc.2024.0546), `code/github_INFORMSJoC_2024.0546/src/Comp/LinTP/main.m` line 76; license file: MIT.

### `fmincon`

Used in 168 of 1084 MATLAB papers (15%) — Solve constrained nonlinear multivariable minimization problem.

Options (share of these 168 papers): `constraints_MDP?` 1%, `constraints_MPCC?` 1%, `constraints_WDP?` 1%, `constraints_eMDP?` 1%.

Most common option set: none; at least one call in 168 papers (100%).

```matlab
          dir=fmincon('QuadObjFun',x,[],[],[],[],lb,ub,[],options, H, g);
```
JPE 2026, [doi:10.1086/741623](https://doi.org/10.1086/741623), `code/dataverse_RWAODQ/PSwarm1.m` line 2819; license file: MIT.

### `fminsearch`

Used in 148 of 1084 MATLAB papers (14%) — Solve unconstrained multivariable local minimization problem using derivative-free method.

Most common option set: none; at least one call in 148 papers (100%).

```matlab
    [sparams, sfval, sexit, ~] = fminsearch(f_obj, [0.5], options);
```
QJE 2025, [doi:10.1093/qje/qjaf018](https://doi.org/10.1093/qje/qjaf018), `code/dataverse_JWCHRZ/analysis_cluster_code_rcnl_supply/estimate_rcnl_supply.m` line 47; license file: MIT.

### `fminunc`

Used in 104 of 1084 MATLAB papers (10%) — Solve unconstrained multivariable nonlinear minimization problem.

Most common option set: none; at least one call in 104 papers (100%).

```matlab
    [parmvec,~,~,~,~,h] = fminunc('normalMLE',theta,options,[],y,x,w);
```
JPE 2025, [doi:10.1086/732526](https://doi.org/10.1086/732526), `code/dataverse_THFJTZ/JPE-Replication-Package_src_estimation-stage1_functions/normalMLEfit.m` line 6; license file: GPL.

### `fminbnd`

Used in 36 of 1084 MATLAB papers (3%) — Solve single-variable local minimization problem on a fixed interval.

Most common option set: none; at least one call in 36 papers (100%).

```matlab
            eta=fminbnd(@(x) fun(x),-10,10);
```
IJOC 2025, [doi:10.1287/ijoc.2022.0375](https://doi.org/10.1287/ijoc.2022.0375), `code/github_INFORMSJoC_2022.0375/code/realistic-portfolio/main.m` line 39; license file: MIT.

### `createOptimProblem`

Used in 11 of 1084 MATLAB papers (1%) — Create optimization problem structure.

Options (share of these 11 papers): `x0` 100%, `objective` 91%, `lb` 82%, `ub` 82%, `options` 73%, `Aineq` 27%, `bineq` 27%, `nonlcon` 18%.

Most common option set: `lb`, `objective`, `options`, `ub`, `x0`; at least one call in 6 papers (55%).

```matlab
    problem_white = createOptimProblem('lsqnonlin','objective',fun_white,'x0',x0,'ub',ub,'lb',lb,'options',lsqnonlin_options);
```
AER 2024, [doi:10.1257/aer.20220234](https://doi.org/10.1257/aer.20220234), `code/code/model/depends/estimate_model.m` line 115.

Next most common option set: `Aineq`, `bineq`, `lb`, `nonlcon`, `objective`, `options`, `ub`, `x0`; at least one call in 2 papers (18%).

```matlab
        problem = createOptimProblem('fmincon','x0',theta_0,...
        'objective',obj_true,'lb',LB_theta,'ub',UB_theta,...
        'nonlcon',constraint_true,'options',options_fmincon,'Aineq', A_theta, 'bineq', b_theta);
```
ReStud 2023, [doi:10.1093/restud/rdad004](https://doi.org/10.1093/restud/rdad004), `code/zenodo_7411193/ARP_replication_code/Code/Simulate_Data/KMSCode/KMSportable_V3/KMS_0_Main.m` lines 649-651.
