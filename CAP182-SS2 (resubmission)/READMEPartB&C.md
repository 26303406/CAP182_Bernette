# CAP182 SS2 — Part B & C (Resubmission)

**Student:** Bernette Lesejane (26303406)
**Notebook:** `Bernette_26303406_CAP182-SS2_PartBandC (Resubmission).ipynb`
**Dataset:** UCI Bank Marketing (`ucimlrepo` id=222) — 45,211 phone-campaign records from a Portuguese bank

---

## Quick Start

1. **Run Cell 2 first** — installs `ucimlrepo` and `xgboost`.
2. Run cells **top to bottom** in order. Each section depends on the previous one.
3. Works in Databricks, Jupyter, Google Colab, or any Python 3.8+ notebook environment.
4. A portable `show()` helper replaces `display()` so the notebook runs anywhere.

---

## Part B — Data Pipeline & Modelling

### 1. Load the Dataset

- Fetches the Bank Marketing dataset via `fetch_ucirepo(id=222)`.
- **Shape:** 45,211 rows × 17 columns.
- **Target:** `y` — did the client subscribe to a term deposit? (yes/no)
- **Class balance:** ~11% yes, ~89% no (highly imbalanced).

### 2. Exploratory Data Analysis (EDA)

| Check | What it covers |
|---|---|
| Structure | Shape, column names, data types |
| Missing values | NaN counts per column (several categorical columns have missing entries) |
| Numeric stats | `describe()` for numeric features |
| Categorical stats | `describe(include='object')` for categorical features |
| Target distribution | Class counts and percentages |
| Leakage evidence | `duration` vs `y` — mean call duration is 537s for "yes" vs 221s for "no" (smoking gun for data leakage) |

### 3. Data Preprocessing

- **Drops `duration`** — this column is only known *after* a call ends, so it leaks the target into the features.
- Separates features (X) from target (y).
- Identifies 6 numeric and 9 categorical columns.
- **80/20 stratified train-test split** (`random_state=42`).
- Builds a `ColumnTransformer`:
  - **Numeric pipeline:** `SimpleImputer` (median) → `StandardScaler`
  - **Categorical pipeline:** `SimpleImputer` (most frequent) → `OneHotEncoder` (handle_unknown='ignore')
- Fits the preprocessor on the training set only (no leakage), then transforms both train and test.

### 4. Feature Engineering

Eight domain-specific features are added to both train and test sets *before* the preprocessor is rebuilt:

| # | Feature | Logic |
|---|---|---|
| 1 | `age_group` | Age binned into life-stage buckets: <25, 25-34, 35-44, 45-54, 55-64, 65+ |
| 2 | `balance_group` | Account balance banded: negative, 0-500, 500-2k, 2k-10k, 10k+ |
| 3 | `was_contacted_before` | Binary flag: `pdays != -1` (was the client ever contacted before this campaign?) |
| 4 | `total_contacts` | `campaign + previous` (overall contact effort) |
| 5 | `prior_success` | Binary flag: `poutcome == 'success'` |
| 6 | `season` | Month mapped to season (winter/spring/summer/autumn) — reduces cardinality |
| 7 | `has_both_loans` | Binary flag: client has both a housing loan and a personal loan |
| 8 | `balance_per_contact` | `balance / campaign` — rough effort-efficiency proxy |

- Feature count goes from 15 → 23 (before encoding) → **70 after one-hot encoding**.
- Preprocessor is rebuilt to include the new features and re-fitted on the training set.

### 5. Modelling

Three classifiers are trained with **class weighting** to handle the ~11% minority class:

| Model | Imbalance Handling | Key Hyperparameters |
|---|---|---|
| Logistic Regression | `class_weight` dict (inverse frequency) | `max_iter=1000` |
| Random Forest | `class_weight='balanced'` | `n_estimators=200` |
| XGBoost | `scale_pos_weight = neg_count / pos_count` | `n_estimators=300`, `learning_rate=0.1`, `max_depth=6`, `subsample=0.8`, `colsample_bytree=0.8` |

- Labels are encoded to 0/1 (`no`→0, `yes`→1) for XGBoost compatibility.
- All models trained on the engineered feature set (70 encoded columns).

### 6. Evaluation — Test-Set Performance

| Model | Accuracy | F1 (yes) | Precision (yes) | Recall (yes) |
|---|---|---|---|---|
| Logistic Regression | 0.755 | 0.373 | 0.27 | 0.62 |
| Random Forest | 0.893 | 0.318 | 0.63 | 0.21 |
| **XGBoost** | **0.838** | **0.459** | **0.38** | **0.59** |

- **XGBoost achieves the best F1 score** (0.459) with the best precision-recall balance.
- Random Forest has high accuracy (0.893) but misses 79% of actual subscribers.
- Logistic Regression has the highest recall (0.62) but very low precision (0.27) — many false positives.

---

## Part C — Performance Metrics & Statistical Measures

### 1. Cross-Validation with Confidence Intervals

- **Method:** `RepeatedStratifiedKFold` — 5-fold × 10 repeats = **50 runs** per model.
- **Metric:** F1 score for the minority class ("yes").
- **95% CI** computed using the t-distribution.

| Model | Mean F1 | Std Dev | 95% CI |
|---|---|---|---|
| Logistic Regression | 0.3733 | 0.0081 | [0.3710, 0.3756] |
| Random Forest | 0.3137 | 0.0154 | [0.3093, 0.3181] |
| **XGBoost** | **0.4458** | **0.0101** | **[0.4430, 0.4487]** |

- XGBoost's CI does not overlap with either competitor — clear separation.

### 2. Pairwise Statistical Comparison

Two tests are run across all three model pairs using the 50 per-fold scores:

#### Paired t-test (parametric)

| Comparison | t-statistic | p-value | Significant? |
|---|---|---|---|
| LR vs RF | +27.381 | < 0.0001 | *** |
| LR vs XGBoost | -52.561 | < 0.0001 | *** |
| RF vs XGBoost | -57.725 | < 0.0001 | *** |

#### Mann–Whitney U test (non-parametric)

| Comparison | U statistic | p-value | Significant? |
|---|---|---|---|
| LR vs RF | 2500.0 | < 0.0001 | *** |
| LR vs XGBoost | 0.0 | < 0.0001 | *** |
| RF vs XGBoost | 0.0 | < 0.0001 | *** |

- **All pairwise comparisons are highly significant** (p < 0.001) under both tests.
- XGBoost is statistically superior to both Logistic Regression and Random Forest.

**Significance levels:** `***` p<0.001  `**` p<0.01  `*` p<0.05  `ns` = not significant

---

## Summary

- **Recommended model:** XGBoost — highest F1 (0.459 test, 0.446 CV), best precision-recall balance, statistically significant superiority (p < 0.001).
- **Key design decisions:** `duration` dropped (data leakage), 8 engineered features added, class weighting applied, stratified train-test split, repeated stratified CV with 95% CIs, paired parametric and non-parametric tests.
- **Notebook is fully portable** — uses `%pip install`, a `show()` helper, and `random_state=42` throughout for reproducibility.