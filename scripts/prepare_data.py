#!/usr/bin/env python3
"""Convenience wrapper to prepare data splits.

Usage:
    python scripts/prepare_data.py
"""
import os
from src.data_prep import main as prep_main

if __name__ == "__main__":
    # Adjust paths if needed
    os.system("python -m src.data_prep --input data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv --outdir data/processed")