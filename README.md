# Telco Churn — TabNet Predictive Retention Analytics

An end‑to‑end business analytics project that cleans and engineers telco customer data, trains **TabNet** and baseline models to predict churn, and translates the outputs into ROI‑aware retention actions.

---

## Why this project matters (business context)
Reducing churn lifts recurring revenue more efficiently than equivalent acquisition spend. This repo shows how to go from **raw operations data → predictive insight → action plan** for **Retention, CX, and Finance** teams.

---

## Problem statement
Identify customers most likely to churn in the next period and explain **why**—so the business can:
- Prioritize outreach to high‑risk segments within capacity constraints
- Tailor retention offers (e.g., contract/price incentives) to the drivers
- Quantify **revenue saved** and **LTV preserved** for budgeting and tradeoffs

---

## Methods & tools (applied analytics)
- **Data cleaning & feature engineering:** type casting, missing values, tenure/plan complexity features
- **Modeling:** Classification Metrics, Logistic Regression, Random Forest, TabNet (deep tabular), Train/Test Split, XGBoost/GBM
- **Evaluation:** ROC AUC, PR AUC, F1, Precision/Recall, **Precision@Top‑N** and **Lift** for capacity‑aware targeting
- **Explainability:** SHAP/feature importances or TabNet attentive masks
- **Delivery:** reproducible notebooks/scripts and saved artifacts for reuse

**Stack detected:** matplotlib, numpy, pandas, pytorch_tabnet, seaborn, shap, sklearn

---

## Repository structure
```
./telco_repo/
└─ telco-churn-tabnet/
   ├─ .git/
   │  ├─ hooks/
   │  │  ├─ applypatch-msg.sample
   │  │  ├─ commit-msg.sample
   │  │  ├─ fsmonitor-watchman.sample
   │  │  ├─ post-update.sample
   │  │  ├─ pre-applypatch.sample
   │  │  ├─ pre-commit.sample
   │  │  ├─ pre-merge-commit.sample
   │  │  ├─ pre-push.sample
   │  │  ├─ pre-rebase.sample
   │  │  ├─ pre-receive.sample
   │  │  ├─ prepare-commit-msg.sample
   │  │  ├─ push-to-checkout.sample
   │  │  ├─ sendemail-validate.sample
   │  │  └─ update.sample
   │  ├─ info/
   │  │  └─ exclude
   │  ├─ logs/
   │  │  ├─ refs/
   │  │  │  ├─ heads/
   │  │  │  │  └─ main
   │  │  │  └─ remotes/
   │  │  │     └─ origin/
   │  │  │        └─ HEAD
   │  │  └─ HEAD
   │  ├─ objects/
   │  │  ├─ info/
   │  │  └─ pack/
   │  │     ├─ pack-d7e37dbf02d9b0e29a778f1ac11ae9d8e11afbea.idx
   │  │     ├─ pack-d7e37dbf02d9b0e29a778f1ac11ae9d8e11afbea.pack
   │  │     └─ pack-d7e37dbf02d9b0e29a778f1ac11ae9d8e11afbea.rev
   │  ├─ refs/
   │  │  ├─ heads/
   │  │  │  └─ main
   │  │  ├─ remotes/
   │  │  │  └─ origin/
   │  │  │     └─ HEAD
   │  │  └─ tags/
   │  ├─ config
   │  ├─ description
   │  ├─ HEAD
   │  ├─ index
   │  └─ packed-refs
   ├─ data/
   │  ├─ raw/
   │  │  └─ WA_Fn-UseC_-Telco-Customer-Churn.csv
   │  ├─ sample/
   │  │  └─ sample_100.csv
   │  └─ README.md
   ├─ docs/
   │  └─ data_dictionary.md
   ├─ notebooks/
   │  ├─ README.md
   │  └─ telco_churn_tabnet_analysis.ipynb
   ├─ scripts/
   │  └─ prepare_data.py
   ├─ src/
   │  ├─ __init__.py
   │  ├─ data_prep.py
   │  └─ model_tabnet.py
   ├─ CITATION.cff
   ├─ LICENSE
   ├─ PROJECT_TREE.txt
   ├─ README.md
   └─ requirements.txt
```

---

## Results & findings (from the dataset you provided)
### Key Results (computed directly from the dataset)

**Dataset size:** 7,043 customers  
**Churned:** 1,869 customers (**26.54%**)

**Tenure (months):**
- Min: 0
- 25th percentile: 9.00
- Median: 29.00
- Mean: 32.37
- 75th percentile: 55.00
- Max: 72

**MonthlyCharges (USD):**
- Overall — mean: 64.76, median: 70.35
- Churned — mean: 74.44, median: 79.65
- Retained — mean: 61.27, median: 64.43

**TotalCharges (USD):**
- Overall — mean: 2283.30, median: 1397.47
- Missing `TotalCharges` values (coerced to NA): 11

#### Churn by Contract Type
| Contract | Customers | ChurnRate_% |
| --- | --- | --- |
| Month-to-month | 3875 | 42.71 |
| Two year | 1695 | 2.83 |
| One year | 1473 | 11.27 |


#### Churn by Internet Service
| InternetService | Customers | ChurnRate_% |
| --- | --- | --- |
| Fiber optic | 3096 | 41.89 |
| DSL | 2421 | 18.96 |
| No | 1526 | 7.40 |


#### Churn by Payment Method
| PaymentMethod | Customers | ChurnRate_% |
| --- | --- | --- |
| Electronic check | 2365 | 45.29 |
| Mailed check | 1612 | 19.11 |
| Bank transfer (automatic) | 1544 | 16.71 |
| Credit card (automatic) | 1522 | 15.24 |


> Notes:  
> - `ChurnRate_%` is the percentage of customers within each group labeled `Churn = Yes`.  
> - `TotalCharges` is converted to numeric; non‑numeric entries in the source file become missing values.

---

## How to run

### 1) Environment
Use Conda or venv (Python 3.10+):
```bash
# conda
conda create -n churn_env python=3.11 -y
conda activate churn_env
```

Install requirements:
```
numpy
pandas
scikit-learn
matplotlib
seaborn
jupyter
imbalanced-learn
shap
pytorch-tabnet
```

### 2) Data
Place the IBM Telco Customer Churn CSV at:
```
data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
```
_(If your repo uses a different path, update the CLI args or notebook cells accordingly.)_

### 3) Train & evaluate
- **Notebooks:** open the training/evaluation notebook(s) under `/notebooks` and run all cells.  
- **Scripts (if present):** check `/scripts` for `prepare_data.py`, `train_baseline.py`, or `train_tabnet.py` and run with `--help` for options.

### 4) Outputs
- **reports/evaluation/** — metrics JSON/CSV + threshold & ROI tables  
- **reports/figures/** — EDA charts, SHAP summaries, TabNet masks  
- **models/** — serialized model artifacts for reuse (git‑ignored)

---

## Interpreting the outputs
- Use the **threshold/ROI** table to pick an operating point that matches outreach capacity and unit economics.  
- **Top‑N targeting** improves retention ROI vs. untargeted campaigns.  
- Pair model drivers with specific plays (e.g., month‑to‑month + high charges → loyalty offer).

---

## Dataset & references
- Dataset: **IBM Telco Customer Churn** (`WA_Fn-UseC_-Telco-Customer-Churn.csv`).  
- Arik & Pfister (2019) *TabNet: Attentive Interpretable Tabular Learning.* arXiv:1908.07442
