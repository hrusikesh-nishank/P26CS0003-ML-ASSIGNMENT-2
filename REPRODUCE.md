# Reproduction Instructions

Run all commands from the repository root.

## 1. Create the Conda environment

```powershell
conda env create -f environment.yml
```

Activate it:

```powershell
conda activate mirnet
```

If the environment already exists, only activate it.

## 2. Alternative installation using pip

```powershell
python -m pip install -r requirements.txt
```

## 3. Start JupyterLab

```powershell
jupyter lab P26CS0003_ML_Assignment_2.ipynb
```

The complete notebook can then be executed using Run All.

## 4. Execute the notebook from PowerShell

```powershell
jupyter nbconvert --to notebook --execute P26CS0003_ML_Assignment_2.ipynb --output reproduced.ipynb --ExecutePreprocessor.timeout=-1
```

Alternatively:

```powershell
.\run_all.ps1
```

## Saved Split

The exact train/validation/test split used in all experiments is:

```text
data/olivetti_split_seed260003.npz
```

## Outputs

Experimental result files are written to:

```text
results/
```

Generated figures are written to:

```text
figures/
```

The bias-variance experiments perform repeated model fitting and require substantially more computation than the earlier experiments.

## Regenerate Figures from Saved Logs

The main numerical figures can be regenerated without rerunning model training:

```powershell
python scripts/make_figures.py
