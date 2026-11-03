# P26CS0003 - Machine Learning Assignment 2

## Overview

This repository contains the code and experimental results for Machine Learning Assignment 2 on the Olivetti Faces dataset.

The experiments include:

- decision tree baseline
- bootstrap aggregation (bagging)
- multiclass SAMME boosting
- clean and masked test-set evaluation
- bias-variance analysis across repeated training-set resampling

## Dataset

The experiments use `fetch_olivetti_faces` from scikit-learn.

- 40 identities
- 10 images per identity
- 64 x 64 grayscale images
- raw flattened pixels only
- no PCA or dimensionality reduction

The seed is `260003`.

Within every identity:

- 6 images are used for training
- 2 images are used for validation
- 2 images are used for testing

The exact split is stored in:

`data/olivetti_split_seed260003.npz`

## Selected Models

### Single Decision Tree

- max_depth = None
- min_samples_leaf = 1

### Bagging

- implemented using bootstrap samples
- final ensemble size = 200 trees

### SAMME Boosting

- weak learner depth = 4
- final number of rounds = 100

## Repository Contents

- `P26CS0003_ML_Assignment_2.ipynb` - complete notebook
- `data/` - saved dataset split
- `results/` - final experimental results
- `figures/` - generated experimental figures
- `scripts/` - figure reproduction script
- `config.json` - experimental configuration
- `requirements.txt` - Python dependencies
- `environment.yml` - Conda environment
- `REPRODUCE.md` - reproduction instructions
- `run_all.ps1` - PowerShell notebook execution command

## Reproduction

See `REPRODUCE.md` for the commands required to recreate the environment and rerun the notebook.

## Author

Hrusikesh Nishank  
Roll Number: P26CS0003
