"""TabNet training scaffold (PyTorch TabNet).

This is a minimal, portfolio-friendly scaffold with TODOs.
For full training, open the notebooks in /notebooks and iterate there first.

Example CLI (once you add your details):
    python -m src.model_tabnet --train data/processed/train.csv --val data/processed/val.csv --target Churn
"""
from __future__ import annotations

import argparse
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pytorch_tabnet.tab_model import TabNetClassifier

# NOTE: You must have torch installed for pytorch-tabnet to work.
# Install PyTorch per your OS from https://pytorch.org/ and then `pip install pytorch-tabnet`.

def prepare_xy(df: pd.DataFrame, target: str):
    """Very simple label-encoding example.
    TODO: Replace with your own preprocessing to handle categoricals robustly."""
    y = df[target].astype(str)
    X = df.drop(columns=[target])

    # Encode target
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Convert categoricals to category codes (TabNet expects numeric tensors)
    for c in X.select_dtypes(include=['object']).columns:
        X[c] = X[c].astype('category').cat.codes

    return X.values, y


def main():
    parser = argparse.ArgumentParser(description="Train TabNet on Telco Churn (scaffold)")
    parser.add_argument("--train", type=str, required=True)
    parser.add_argument("--val", type=str, required=True)
    parser.add_argument("--target", type=str, default="Churn")
    args = parser.parse_args()

    train_df = pd.read_csv(args.train)
    val_df = pd.read_csv(args.val)

    X_train, y_train = prepare_xy(train_df, args.target)
    X_val, y_val = prepare_xy(val_df, args.target)

    # TODO: Tune your hyperparameters
    clf = TabNetClassifier()
    clf.fit(
        X_train, y_train,
        eval_set=[(X_val, y_val)],
        eval_name=['val'],
        max_epochs=10,  # TODO: increase
        patience=3,
        batch_size=1024,
        virtual_batch_size=128,
    )

    # TODO: Save model, log metrics, and export plots
    print("Training complete (scaffold).")


if __name__ == "__main__":
    main()