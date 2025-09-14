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


    ## What I Learned (suggested talking points)
    - Why TabNet for tabular data and how it differs from tree‑based methods.

    - Handling messy columns (e.g., `TotalCharges`) and class imbalance.

    - Turning exploratory notebooks into reusable modules.


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
