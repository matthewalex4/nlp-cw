# NLP Coursework: PCL Detection

This repository contains experiments for binary detection of Patronizing and Condescending Language (PCL) on the SemEval-2022 Task 4 dataset. This constitutes the coursework for the Natural Language Processing Module at Imperial College London in 2025/26.

## Project Structure

- `BestModel/`: Main training/evaluation notebooks and saved model artifacts.
- `BestModel/models/`: Stored transformer checkpoints for DeBERTa and RoBERTa experiments.
- `BestModel/ablation_results/`: Outputs from ablation variants (`no_aug`, `no_key`, `unb`).

- `data/`: Original SemEval Task 4 data files used for training, development, and test inference.
- `utils/`: Shared helper code for loading data and computing evaluation metrics.

- `eda/`: Exploratory Data Analysis notebook and visualizations.

- `labels/ref/`: Reference labels for evaluation on development splits.
- `labels/res/`: Model prediction outputs for development and test sets.

## Environment Setup

This project uses Python and Jupyter notebooks.

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install core dependencies. This can be done inside Jupyter by running the first cell of `main.ipynb`.

## Data

The repository already includes the SemEval files under `data/`:
- `dontpatronizeme_pcl.tsv`
- `train_semeval_parids-labels.csv`
- `dev_semeval_parids-labels.csv`
- `task4_test.tsv`

## Predictions

Predictions for the development set are found in `labels/res/dev.txt`. Likewise, predictions for the test set are in `labels/res/test.txt`.
