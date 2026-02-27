# NLP Coursework: PCL Detection

This repository contains experiments for binary detection of Patronizing and Condescending Language (PCL) on the SemEval-2022 Task 4 dataset. This constitutes the coursework for the Natural Language Processing Module at Imperial College London in 2025/26.

The main workflow is notebook-based:
- `main.ipynb`: training, evaluation, ensembling, and ablations
- `eda.ipynb`: exploratory data analysis

## Project Structure

- `data/`: dataset files (`dontpatronizeme_pcl.tsv`, train/dev IDs, test file)
- `load_data.py`: helper class for loading and binarizing labels ({0,1}->0, {2,3,4}->1)
- `evaluation.py`: SemEval-style scorer (precision, recall, F1)
- `ref/`: reference labels used during local evaluation
- `res/`: prediction files used during local evaluation/submission format
- `final_results/`, `ablation_results/`: saved model checkpoints and experiment outputs

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

Predictions for the development set are found in `res/dev.txt`. Likewise, predictions for the test set are in `res/test.txt`.

BestModel
  models/
    Roberta/
      checkpoint-5160/
        config.json
        pytorch_model.bin
        tokenizer_config.json
        vocab.json
        merges.txt
    Deberta/
      checkpoint-2064/
        config.json
        pytorch_model.bin
        tokenizer_config.json
        vocab.txt
  labels/
    dev.txt
    test.txt
  main.ipynb
utils/
  evaluation.py
  load_data.py
data/
  dontpatronizeme_pcl.tsv
  train_semeval_parids-labels.csv
  dev_semeval_parids-labels.csv
  task4_test.tsv
eda/
  eda.ipynb
  misc.jpg
README.md
