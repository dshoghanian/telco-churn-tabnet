# Telco Customer Churn — Predictive Retention Analytics (Business Analytics Portfolio)

**One‑line summary:** An end‑to‑end business analytics project that cleans and engineers telco customer data, builds predictive models to identify churn risk, and translates model outputs into concrete, ROI‑focused retention actions for business stakeholders.

---

## Why this project matters (Business context)
Customer churn directly impacts recurring revenue. Improving retention even slightly can outperform equivalent spend on acquisition. This project shows how to:
- Turn raw operational data into actionable insights for **Retention, CX, and Finance** teams.
- **Predict** which customers are at risk of leaving in the next period.
- **Explain** what drives churn to shape offers, product fixes, and outreach.
- **Quantify impact** (e.g., revenue saved, lifetime value preserved) to prioritize interventions and budgets.

> Target audience: Hiring managers and teams looking for business‑savvy analysts who can move from data wrangling to stakeholder‑ready decisions.

---

## What the project does (End‑to‑end workflow)
1. **Data ingestion & cleaning**  
   - Source: *IBM Telco Customer Churn* (included as `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`).  
   - Handles missing values (e.g., `TotalCharges`), trims/corrects label values (e.g., `Churn`), normalizes column types, and standardizes categories.

2. **Feature engineering**
   - Customer tenure features, plan complexity, add‑on services bundles, payment frictions, price‑to‑value indicators (e.g., `MonthlyCharges` vs. services).
   - Encodes high‑cardinality/categorical fields while keeping interpretability.

3. **Exploratory analysis & data storytelling**
   - Clear visuals that tie patterns to decisions (e.g., higher risk in month‑to‑month contracts).  
   - Stakeholder‑ready annotations to guide action, not just show charts.

4. **Modeling (statistical + ML)**
   - Baselines: Logistic Regression / Regularized GLM for interpretability.
   - Tree‑based: Random Forest, Gradient Boosting / XGBoost for non‑linear signal.
   - **Deep tabular**: TabNet for joint performance + interpretability via attentive feature masks.
   - Class imbalance strategies (e.g., stratified CV, weighted loss, or SMOTE).

5. **Evaluation and business framing**
   - Core metrics: ROC AUC, PR AUC, F1, Precision/Recall.  
   - Business metrics: **Precision@Top‑N%**, **Lift**, **Retention Uplift**, and **Estimated Revenue Saved** given a contact budget and average CLV.  
   - **Threshold tuning** aligned to treatment capacity and cost/benefit assumptions.

6. **Explainability & actionability**
   - Global & local importance (e.g., SHAP) + TabNet attentive masks.
   - Playbooks for interventions (e.g., loyalty offer for month‑to‑month + high charges).

7. **Delivery & reuse**
   - Reproducible notebooks & scripts.
   - Saved artifacts (figures, evaluation reports, and model files) for reuse in dashboards or downstream apps.

---

## Key results (fill in with your actual numbers)
> Replace the placeholders below with your run results to make this portfolio piece shine.

- **ROC AUC:** `...`  
- **PR AUC:** `...`  
- **F1 (selected threshold):** `...`  
- **Precision@Top 10% (or capacity‑matched):** `...`  
- **Lift@Top 10%:** `...`  
- **Estimated monthly revenue saved:** `...` (assumptions: average CLV = `...`, outreach capacity = `...`, offer cost = `...`)

**What it means for the business:** With capacity‑aware targeting and a simple retention playbook, the model can focus outreach on the most at‑risk customers and improve ROI vs. untargeted campaigns. Threshold choice is guided by treatment limits and economics (not just accuracy).

---

## Repository structure

```
.
├─ notebooks/
│  ├─ 01_eda_data_quality.ipynb            # Explore data, missingness, leakage checks, stakeholder‑friendly visuals
│  ├─ 02_feature_engineering.ipynb         # Build domain features and encodings
│  ├─ 03_modeling_baselines.ipynb          # Logistic/GLM + tree baselines with CV and metrics
│  ├─ 04_modeling_tabnet.ipynb             # Deep tabular (TabNet) + interpretation masks
│  └─ 05_explainability_business.ipynb     # SHAP, threshold tuning, ROI framing, and “what‑to‑do” playbook
│
├─ src/
│  ├─ __init__.py
│  ├─ data_prep.py                         # Cleaning, validation, type casting, categorical handling
│  ├─ features.py                          # Feature generation utilities
│  ├─ train.py                             # Common training loop, CV, logging
│  ├─ metrics.py                           # Technical + business metrics (Lift, Precision@N, cost curves)
│  └─ explain.py                           # SHAP, partial dependence, TabNet masks export
│
├─ scripts/
│  ├─ prepare_data.py                      # CLI for transforming raw → processed
│  ├─ train_baseline.py                    # CLI for baselines
│  └─ train_tabnet.py                      # CLI for TabNet
│
├─ data/
│  ├─ raw/                                 # Place original CSV here (e.g., WA_Fn-UseC_-Telco-Customer-Churn.csv)
│  ├─ interim/                             # Intermediate checks
│  ├─ processed/                           # Cleaned parquet/CSV ready for modeling
│  └─ external/                            # Optional: SQL extracts or other sources
│
├─ models/                                 # Saved models (git‑ignored)
├─ reports/
│  ├─ figures/                             # PNG/SVG exported charts for README / decks
│  └─ evaluation/                          # Metrics JSON/CSV + threshold & ROI tables
├─ logs/                                   # Training and experiment logs (git‑ignored)
├─ requirements.txt
├─ .gitignore
└─ README.md
```

> If your existing repo uses slightly different filenames (e.g., `model_tabnet.py`), keep the layout but adjust names in this README for accuracy.

---

## How to run the analysis

### 1) Environment setup
```bash
# Option A: Conda
conda create -n churn_env python=3.11 -y
conda activate churn_env

# Option B: venv
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Minimal `requirements.txt` (edit as needed):
```
pandas
numpy
scikit-learn
matplotlib
seaborn
xgboost
shap
pytorch-lightning>=2.0  # if using TabNet with PyTorch
torch                   # CPU CUDA optional
tabnet                  # or pytorch‑tabnet variant
imbalanced-learn
pyyaml
```

### 2) Data
Place the original file at:
```
data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
```
> (If you already have the file in your repo root, move or copy it into `data/raw/`.)

### 3) Prepare cleaned dataset
```bash
python scripts/prepare_data.py \
  --in_path data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv \
  --out_path data/processed/churn_clean.parquet
```

### 4) Run baselines
```bash
python scripts/train_baseline.py \
  --data data/processed/churn_clean.parquet \
  --config configs/baseline.yaml \
  --out_dir reports/evaluation/baseline
```

### 5) Train TabNet (optional, for deep tabular + interpretability)
```bash
python scripts/train_tabnet.py \
  --data data/processed/churn_clean.parquet \
  --config configs/tabnet.yaml \
  --out_dir reports/evaluation/tabnet
```

### 6) Notebooks
Open the notebooks to explore EDA, feature engineering, modeling, and business framing:
```bash
jupyter lab
# then run notebooks in the order 01 → 05
```

---

## Interpreting the outputs

- **reports/evaluation/**  
  - `metrics.json` with ROC AUC, PR AUC, F1, Precision/Recall, **Precision@N**, **Lift**, and threshold/ROI tables.  
  - Use the **threshold table** to select an operating point that matches your contact capacity & economics.

- **reports/figures/**  
  - EDA visuals (e.g., churn by contract type), SHAP summaries, and TabNet attentive masks to illustrate drivers.  
  - Include 2–3 **stakeholder‑ready** figures in your README/deck (story‑first captions).

- **models/**  
  - Serialized models for reuse (`.pkl` or `.pt`). Can be plugged into an app, batch score, or BI export.

- **Dashboards (optional)**  
  - Export top‑N lists with recommended actions to Tableau/Power BI for field teams or CX ops.

---

## How this demonstrates Business Analytics skills

- **Data storytelling & visualization** — EDA and final charts include business‑first annotations and takeaways.  
- **Statistical & predictive modeling** — Strong baselines + advanced models; clear comparison and rationale.  
- **From raw data to insight** — Rigorous cleaning, leakage checks, and features tied to telco realities.  
- **Communicating to stakeholders** — Threshold/ROI framing, capacity‑aware targeting, and “what‑to‑do” guides.  
- **Reproducibility & handoff** — Scripts/notebooks, logged configs/metrics, and saved artifacts for production/LTV teams.

---

## Dataset & attribution
- Dataset: **IBM Telco Customer Churn** (`WA_Fn-UseC_-Telco-Customer-Churn.csv`).  
- If you use **TabNet** for modeling/interpretability, cite the original paper in your repo/docs.

---

## References
- Arik, S. O., & Pfister, T. (2019). *TabNet: Attentive Interpretable Tabular Learning*. arXiv:1908.07442. https://arxiv.org/abs/1908.07442

