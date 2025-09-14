"""Data preparation utilities for the Telco Churn project.

Run from CLI:
    python -m src.data_prep --input data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv --outdir data/processed

This script intentionally stays light and leaves TODOs for personalization.
"""
from __future__ import annotations

import argparse
import os
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


def load_raw(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Minimal cleaning: strip whitespace, coerce TotalCharges, drop duplicates.

    TODO: Add your own feature engineering (e.g., tenure bins, combined services, etc.).
    """
    df = df.copy()

    # Trim string columns
    for c in df.select_dtypes(include='object').columns:
        df[c] = df[c].astype(str).str.strip()

    # Special case: TotalCharges has blanks -> coerce to float
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Drop duplicate rows if any
    df = df.drop_duplicates()

    return df


def train_val_test_split(
    df: pd.DataFrame,
    target: str = 'Churn',
    test_size: float = 0.2,
    val_size: float = 0.1,
    random_state: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Create train/val/test splits with stratification on the target."""
    stratify = df[target] if target in df.columns else None
    train_df, temp_df = train_test_split(
        df, test_size=(test_size + val_size), random_state=random_state, stratify=stratify
    )

    remaining = test_size + val_size
    val_fraction = val_size / remaining if remaining > 0 else 0.5

    stratify_temp = temp_df[target] if target in temp_df.columns else None
    val_df, test_df = train_test_split(
        temp_df, test_size=(1 - val_fraction), random_state=random_state, stratify=stratify_temp
    )

    return train_df, val_df, test_df


def main():
    parser = argparse.ArgumentParser(description="Prepare data for Telco Churn (TabNet)")
    parser.add_argument("--input", type=str, required=True, help="Path to raw CSV")
    parser.add_argument("--outdir", type=str, default="data/processed", help="Output directory for splits")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    df = load_raw(args.input)
    df = basic_clean(df)

    # TODO: Consider additional cleaning/feature engineering here.
    # e.g., encoding categorical variables if you plan to train scikit-learn baselines in scripts.

    train_df, val_df, test_df = train_val_test_split(df)

    train_df.to_csv(os.path.join(args.outdir, "train.csv"), index=False)
    val_df.to_csv(os.path.join(args.outdir, "val.csv"), index=False)
    test_df.to_csv(os.path.join(args.outdir, "test.csv"), index=False)

    print(f"Saved splits to {args.outdir}")


if __name__ == "__main__":
    main()