# Python examples from published replication packages

Commands and functions related to this skill, as written in the author code of 864 Python replication packages from 13 economics, finance, management, operations research and statistics journals (call database built 2026-10-19). Shares count papers. Frequent use is a description of practice, not a recommendation; the skill and `harness/paradigms/` state when a choice applies.

Each excerpt is copied verbatim from the cited package; reuse follows that package's license.

### `torch.nn.Linear`

Used in 104 of 864 Python papers (12%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Options (share of these 104 papers): `bias` 22%, `in_features` 6%, `out_features` 6%.

Most common option set: none; at least one call in 98 papers (94%).

```python
model.fc2 = nn.Linear(d, 2)
```
JRSSB 2026, [doi:10.1093/jrsssb/qkaf062](https://doi.org/10.1093/jrsssb/qkaf062), `code/github_JZHANG4362_Additive-Effect-Assisted-Learning/car_data/test1_transfer_1.py` line 335; license file: MIT.

Next most common option set: `bias`; at least one call in 21 papers (20%).

```python
        self.reg_lin = nn.Linear(3, k * 3, bias=False)
```
JASA 2026, [doi:10.1080/01621459.2026.2621515](https://doi.org/10.1080/01621459.2026.2621515), `code/github_XiaoyuMa94_Conditional-XVAE/Simulation/train_cXVAE.py` line 202; license file: MIT.

### `torch.nn.Sequential`

Used in 62 of 864 Python papers (7%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Most common option set: none; at least one call in 62 papers (100%).

```python
        self.shortcut = nn.Sequential()
```
IJOC 2026, [doi:10.1287/ijoc.2024.0991](https://doi.org/10.1287/ijoc.2024.0991), `code/github_INFORMSJoC_2024.0991/model/resnet_basicblock.py` line 64; license file: MIT.

### `torch.nn.ReLU`

Used in 60 of 864 Python papers (7%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Options (share of these 60 papers): `inplace` 27%.

Most common option set: none; at least one call in 52 papers (87%).

```python
            nn.ReLU(),
```
IJOC 2026, [doi:10.1287/ijoc.2023.0115](https://doi.org/10.1287/ijoc.2023.0115), `code/github_INFORMSJoC_2023.0115/scripts/graph_encoder_edge_weighted.py` line 105; license file: MIT.

Next most common option set: `inplace`; at least one call in 16 papers (27%).

```python
        self.relu = nn.ReLU(inplace=True)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0448](https://doi.org/10.1287/ijoc.2023.0448), `code/github_INFORMSJoC_2023.0448/stage2/calibration.py` line 756; license file: MIT.

### `torch.utils.data.DataLoader`

Used in 59 of 864 Python papers (7%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Options (share of these 59 papers): `batch_size` 100%, `shuffle` 93%, `num_workers` 32%, `drop_last` 25%, `dataset` 20%, `pin_memory` 19%, `sampler` 17%, `collate_fn` 14%, `**` 3%.

Most common option set: `batch_size`, `shuffle`; at least one call in 38 papers (64%).

```python
    test_loader = DataLoader(val_dataset, batch_size=32,shuffle=True)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0508](https://doi.org/10.1287/ijoc.2023.0508), `code/github_INFORMSJoC_2023.0508/src/attack_evaluate.py` line 181; license file: MIT.

### `torch.nn.Dropout`

Used in 44 of 864 Python papers (5%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Options (share of these 44 papers): `p` 36%.

Most common option set: none; at least one call in 34 papers (77%).

```python
        self.drop = nn.Dropout()
```
IJOC 2026, [doi:10.1287/ijoc.2024.1017](https://doi.org/10.1287/ijoc.2024.1017), `code/github_INFORMSJoC_2024.1017/src/model/charlstm.py` line 15; license file: MIT.

Next most common option set: `p`; at least one call in 16 papers (36%).

```python
        learner = nn.Sequential(nn.Dropout(p=p), nn.Linear(n_t, n_hidden), nn.LeakyReLU(),
```
JRSSB 2026, [doi:10.1093/jrsssb/qkaf075](https://doi.org/10.1093/jrsssb/qkaf075), `code/github_syrgkanislab_npiv_functionals/notebooks/all_experiments.py` line 101; license file: MIT.

### `torch.nn.functional.relu`

Used in 44 of 864 Python papers (5%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Options (share of these 44 papers): `inplace` 5%.

Most common option set: none; at least one call in 43 papers (98%).

```python
        out = F.relu(out)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0514](https://doi.org/10.1287/ijoc.2023.0514), `code/github_INFORMSJoC_2023.0514/scripts/MMTRAL-/backbone.py` line 60; license file: MIT.

### `torch.optim.Adam`

Used in 38 of 864 Python papers (4%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Options (share of these 38 papers): `lr` 95%, `weight_decay` 37%, `betas` 18%, `eps` 5%.

Most common option set: `lr`; at least one call in 23 papers (61%).

```python
                name: optim.Adam(model.parameters(), lr=0.001)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0130](https://doi.org/10.1287/ijoc.2023.0130), `code/github_INFORMSJoC_2023.0130/src/ml_sk_implementation.py` line 199; license file: MIT.

Next most common option set: `lr`, `weight_decay`; at least one call in 9 papers (24%).

```python
    optimizer  = optim.Adam(model.parameters(), lr=lr, weight_decay=wd)
```
IJOC 2026, [doi:10.1287/ijoc.2023.0493](https://doi.org/10.1287/ijoc.2023.0493), `code/github_INFORMSJoC_2023.0493/scripts/evaluate.py` line 229; license file: MIT.

### `torch.nn.Conv2d`

Used in 34 of 864 Python papers (4%) — Tensors and Dynamic neural networks in Python with strong GPU acceleration.

Options (share of these 34 papers): `kernel_size` 79%, `padding` 65%, `stride` 59%, `bias` 35%, `out_channels` 26%, `in_channels` 24%, `dilation` 9%, `groups` 9%, `**` 6%.

Most common option set: none; at least one call in 17 papers (50%).

```python
        self.conv1 = nn.Conv2d(3, 6, 5)
```
IJOC 2026, [doi:10.1287/ijoc.2025.1443](https://doi.org/10.1287/ijoc.2025.1443), `code/github_INFORMSJoC_2025.1443/src/models/model.py` line 9; license file: MIT.

Next most common option set: `bias`, `kernel_size`, `padding`, `stride`; at least one call in 9 papers (26%).

```python
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3,
                               bias=False)
```
JASA 2026, [doi:10.1080/01621459.2026.2719040](https://doi.org/10.1080/01621459.2026.2719040), `code/github_jindongwang_transferlearning/code/deep/DeepMEDA/ResNet.py` lines 100-101; license file: MIT.
