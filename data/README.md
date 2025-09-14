# Data Folder

- `sample/sample_100.csv` — A tiny (100‑row) sample of the IBM Telco Customer Churn dataset to keep the repo light for your portfolio.
- The **full** dataset file should be placed at: `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv` (this path is *git‑ignored* by default).

## Get the dataset
You likely obtained the file as `WA_Fn-UseC_-Telco-Customer-Churn.csv`. Verify the license from your source before committing the full CSV to a public repo.

## Notes
- Many projects drop the `customerID` column.
- The `TotalCharges` column may contain blanks; coerce to numeric with `errors='coerce'`.