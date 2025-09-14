**Rows**: 7043  
**Columns**: 21

## Columns Overview

| Column | Dtype | Non-Null | Unique | Missing | Notes |

|---|---:|---:|---:|---:|---|

| customerID | object | 7043 | 7043 | 0 | Unique identifier; often dropped from modeling. |
| gender | object | 7043 | 2 | 0 |  |
| SeniorCitizen | int64 | 7043 | 2 | 0 |  |
| Partner | object | 7043 | 2 | 0 |  |
| Dependents | object | 7043 | 2 | 0 |  |
| tenure | int64 | 7043 | 73 | 0 |  |
| PhoneService | object | 7043 | 2 | 0 |  |
| MultipleLines | object | 7043 | 3 | 0 |  |
| InternetService | object | 7043 | 3 | 0 |  |
| OnlineSecurity | object | 7043 | 3 | 0 |  |
| OnlineBackup | object | 7043 | 3 | 0 |  |
| DeviceProtection | object | 7043 | 3 | 0 |  |
| TechSupport | object | 7043 | 3 | 0 |  |
| StreamingTV | object | 7043 | 3 | 0 |  |
| StreamingMovies | object | 7043 | 3 | 0 |  |
| Contract | object | 7043 | 3 | 0 |  |
| PaperlessBilling | object | 7043 | 2 | 0 |  |
| PaymentMethod | object | 7043 | 4 | 0 |  |
| MonthlyCharges | float64 | 7043 | 1585 | 0 |  |
| TotalCharges | object | 7043 | 6531 | 0 | Numeric but may contain blanks; coerce to float. |
| Churn | object | 7043 | 2 | 0 | Target (Yes/No). |

## Top Values (Categorical)

**customerID**

| Value | Count |
|---|---:|
| 7590-VHVEG | 1 |
| 3791-LGQCY | 1 |
| 6008-NAIXK | 1 |
| 5956-YHHRX | 1 |
| 5365-LLFYV | 1 |

**gender**

| Value | Count |
|---|---:|
| Male | 3555 |
| Female | 3488 |

**Partner**

| Value | Count |
|---|---:|
| No | 3641 |
| Yes | 3402 |

**Dependents**

| Value | Count |
|---|---:|
| No | 4933 |
| Yes | 2110 |

**PhoneService**

| Value | Count |
|---|---:|
| Yes | 6361 |
| No | 682 |

**MultipleLines**

| Value | Count |
|---|---:|
| No | 3390 |
| Yes | 2971 |
| No phone service | 682 |

**InternetService**

| Value | Count |
|---|---:|
| Fiber optic | 3096 |
| DSL | 2421 |
| No | 1526 |

**OnlineSecurity**

| Value | Count |
|---|---:|
| No | 3498 |
| Yes | 2019 |
| No internet service | 1526 |

**OnlineBackup**

| Value | Count |
|---|---:|
| No | 3088 |
| Yes | 2429 |
| No internet service | 1526 |

**DeviceProtection**

| Value | Count |
|---|---:|
| No | 3095 |
| Yes | 2422 |
| No internet service | 1526 |

**TechSupport**

| Value | Count |
|---|---:|
| No | 3473 |
| Yes | 2044 |
| No internet service | 1526 |

**StreamingTV**

| Value | Count |
|---|---:|
| No | 2810 |
| Yes | 2707 |
| No internet service | 1526 |

**StreamingMovies**

| Value | Count |
|---|---:|
| No | 2785 |
| Yes | 2732 |
| No internet service | 1526 |

**Contract**

| Value | Count |
|---|---:|
| Month-to-month | 3875 |
| Two year | 1695 |
| One year | 1473 |

**PaperlessBilling**

| Value | Count |
|---|---:|
| Yes | 4171 |
| No | 2872 |

**PaymentMethod**

| Value | Count |
|---|---:|
| Electronic check | 2365 |
| Mailed check | 1612 |
| Bank transfer (automatic) | 1544 |
| Credit card (automatic) | 1522 |

**TotalCharges**

| Value | Count |
|---|---:|
|   | 11 |
| 20.2 | 11 |
| 19.75 | 9 |
| 20.05 | 8 |
| 19.9 | 8 |

**Churn**

| Value | Count |
|---|---:|
| No | 5174 |
| Yes | 1869 |
