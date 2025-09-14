# Telco Customer Churn — TabNet (PyTorch)

    A clean, portfolio‑ready repo showcasing a modern deep‑learning approach (TabNet) on the classic IBM Telco Customer Churn dataset. It includes notebooks, minimal source code scaffolding, and documentation to reproduce results and extend the project.

    ## Key Features
    - End‑to‑end flow: data prep → feature engineering → model training & evaluation (TabNet).

    - Clear, modular structure (`src/`, `notebooks/`, `data/`, `docs/`).

    - Lightweight scripts with TODOs so you can make it your own.

    - Data dictionary and a 100‑row sample to keep the repo lean.


    ## Pipeline (Mermaid)
    ```mermaid
    flowchart LR
      A[CSV: Telco Churn] --> B[Data Prep]
      B --> C[Train/Validation/Test Split]
      C --> D[TabNet Classifier]
      D --> E[Evaluation + Explainability]
      E --> F[Reports/figures]
    ```

    ## Project Structure
    ```
    telco-churn-tabnet/
├─ notebooks/
│  ├─ TabNet.ipynb
│  ├─ telco_churn_tabnet_analysis.ipynb
│  └─ README.md
├─ src/
│  ├─ __init__.py
│  ├─ data_prep.py
│  └─ model_tabnet.py
├─ scripts/
│  └─ prepare_data.py
├─ data/
│  ├─ README.md
│  └─ sample/
│     └─ sample_100.csv
├─ docs/
│  └─ data_dictionary.md
├─ reports/
│  └─ figures/.gitkeep
├─ models/ (git-ignored)
├─ logs/   (git-ignored)
├─ requirements.txt
├─ .gitignore
├─ LICENSE
├─ CITATION.cff
└─ README.md
    ```

    ## Quickstart

    1. **Create & activate a virtual environment** (conda or venv).
    2. **Install PyTorch** per your OS/accelerator from https://pytorch.org/.
    3. Install the rest of the deps:
       ```bash
       pip install -r requirements.txt
       ```
    4. Start Jupyter:
       ```bash
       jupyter lab
       ```
    5. Open the notebooks in `notebooks/` and run them.

    ### Data
    - Local path expected for full dataset: `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv` (git‑ignored).
    - This repo ships a tiny sample at `data/sample/sample_100.csv` to keep things light.
    - **License note:** verify the dataset’s license from your original source before committing the full CSV to a public repo.

    ### Reproduce (CLI option)
    ```bash
    # Create train/val/test splits (optional)
    python -m src.data_prep --input data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv --outdir data/processed

    # (Scaffold) Train TabNet once you add your details
    python -m src.model_tabnet --train data/processed/train.csv --val data/processed/val.csv --target Churn
    ```

## Results

- **Accuracy (TabNet, test set):** `0.78`
- **ROC AUC (TabNet, test set):** `0.8177`
- **Confusion matrix (TN, FP / FN, TP):**


    ## What I Learned

- **Why TabNet for tabular data (vs. tree-based methods):**
- TabNet uses **sequential attention** and **sparse feature masks** (“decision steps”) to focus on the most relevant columns at each step.  
- Compared with Random Forest/XGBoost (ensembles of decision trees), TabNet gives **built-in interpretability** (mask importances) and can work well with **less hand-crafted feature engineering**.  
- In this dataset, TabNet’s ROC AUC (`~0.818`) was slightly behind Logistic Regression (`~0.836`), but its **explanations** and sparse attention provide valuable insight for stakeholders.

- **Handling messy columns & mild class imbalance:**
- `TotalCharges` comes in as text with blanks; I coerced it to numeric using `pd.to_numeric(..., errors='coerce')` and dropped NAs before modeling.
- I removed the identifier `customerID` and **one-hot encoded** categorical features with `pd.get_dummies`.
- The dataset is **imbalanced** (~26.5% churn). I evaluated with **ROC AUC** (not just accuracy) to account for the skew; thresholds can be tuned later to meet business precision/recall trade-offs.

- **Turning exploratory notebooks into reusable modules:**
- I separated reusable steps into `src/` (e.g., `src/data_prep.py` for cleaning/splitting; `src/model_tabnet.py` as a training scaffold) and created a small script in `scripts/` to run data prep.
- I kept heavy/raw data **git-ignored** and shipped a **100‑row sample** for quick iteration.
- I added a **data dictionary**, **MIT license**, and **CITATION.cff** so the project is portfolio-ready and reproducible.


    ## How to Publish on GitHub
    ```bash
    cd telco-churn-tabnet
    git init
    git add .
    git commit -m "Initial commit: TabNet Telco Churn"
    git branch -M main

    # Option A: GitHub CLI (recommended)
    gh repo create <your-username>/telco-churn-tabnet --public --source=. --remote=origin --push

    # Option B: Manual remote
    git remote add origin git@github.com:<your-username>/telco-churn-tabnet.git
    git push -u origin main
    ```

    ## License
    MIT © 2025 Dante Shoghanian

    ## Citation
    See `CITATION.cff`.
