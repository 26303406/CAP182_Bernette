# CAP182 SS3 - STADIOEquities Account Activation Model

## Project overview

This repository contains the end-to-end workflow for the SS3 project: predicting whether a STADIOEquities account will make its first deposit within 90 days of registration.

The business goal is to identify accounts that are likely to stall during onboarding or fail to activate, so that outreach and onboarding support can be targeted before value is lost.

## Business problem

STADIOEquities loses a meaningful share of value between registration and first deposit. The project addresses one key question:

> Will this account make its first deposit within 90 days of registration?

Outcome variable:

- `activated = 1`: first deposit occurs within 90 days
- `activated = 0`: no first deposit within 90 days

The modelling task is a supervised binary classification problem using account-level data from the client extract.

## Project objective

Build a predictive model that can:

- predict account activation risk early,
- rank accounts by likely failure to activate,
- support targeted nudges, onboarding interventions, and retention strategy,
- avoid data leakage and evaluate fairly on unseen data.

## End-to-end workflow

1. Data audit and table assessment
2. Data cleaning and preprocessing
3. Feature engineering and account-level aggregation
4. Train/validation/test splitting
5. Model training with SS2-aligned methods
6. Performance evaluation and business validation
7. Results visualisation and reporting

## Repository structure

- `SS3_PartB.ipynb` - the single required SS3 Part B notebook; contains the end-to-end analysis
- `00_Project_Setup.ipynb` - optional environment and shared-import check
- `preprocessing/`, `feature-extraction/`, `modelling/`, `evaluation/` - earlier notebooks retained as reference; they are not required to complete SS3 Part B
- `utils/` - shared imports and reusable helpers
- `results/` - saved metrics, tables, and figures
- `artifacts/` - trained models, preprocessors, and split outputs
- `data/` - raw client data files
- `client reports/` - business documentation and project brief
- `dashboards/` - dashboard outputs and supporting views
- `visualisation/` - plotting and reporting assets
- `retraining/` - retraining workflow assets

## SS3 Part B notebook

The assignment deliverable is one notebook: `SS3_PartB.ipynb`. Run its cells from top to bottom. It covers the complete workflow:

1. Load and audit the client tables
2. Select relevant data and define the activation target
3. Clean and prepare account-level features
4. Split data into training, validation, and unseen test sets
5. Train and save the Random Forest, XGBoost, and ensemble models
6. Evaluate performance and business usefulness
7. Create and save visualisations

The notebooks in the workflow folders are retained as earlier project work and examples. They are not prerequisites for running or submitting `SS3_PartB.ipynb`.

## Modelling approach

The project uses a SS2-aligned ensemble strategy:

- SMOTE on the training set to address class imbalance
- Random Forest classifier
- XGBoost classifier
- Ensemble probability averaging
- Decision threshold set at 0.5 unless validation suggests otherwise

Important modelling safeguards:

- preprocessing is fit only on the training data
- validation is used for model monitoring, not tuning
- the unseen test set is used only for final evaluation
- leakage columns are removed before modelling

## Data quality considerations

The project explicitly checks for:

- exact duplicate accounts,
- missing and structurally blank values,
- inconsistent category spelling or casing,
- mixed date formats,
- leakage from post-deposit or label-derived fields,
- timing-sensitive fields that could distort evaluation if used incorrectly.

## Output files

The project saves results into these folders:

- `results/` - summary tables and metrics
- `results/figures/` - charts and visual diagnostics
- `artifacts/` - fitted preprocessing objects and trained models
- `dashboards/` - visual deliverables for business communication

## Technical stack

- Python
- pandas
- NumPy
- scikit-learn
- XGBoost
- imbalanced-learn
- Matplotlib
- Seaborn
- Jupyter Notebooks

## Shared notebook imports

Common Python imports are maintained in `utils/notebook_imports.py`. Each analysis notebook loads them with:

```python
from utils.notebook_imports import *
```

This keeps common imports consistent. Add any new shared dependency to `requirements.txt` and to the shared module's exports. Keep notebook-specific imports local if they are not used elsewhere.

## How to run

From the repository root, create and activate a virtual environment, then install the pinned dependencies listed in `requirements.txt`:

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

Start Jupyter from the repository root so Python can resolve `utils/notebook_imports.py`. Open `SS3_PartB.ipynb` and run its cells from top to bottom. The optional `00_Project_Setup.ipynb` can be used to check the environment, but it is not part of the required analysis flow. Each notebook uses its own kernel; running the setup notebook does not transfer imports or variables to `SS3_PartB.ipynb`.

## Expected outcome

The final output is a model that can rank accounts by activation likelihood and highlight the accounts most likely to stall. This supports the business decision of prioritising onboarding nudges, support, and education where they are most likely to improve activation rates.

## Summary

This project combines data cleaning, feature engineering, predictive modelling, and business validation into one workflow designed to answer a practical problem for STADIOEquities: how to identify accounts likely to fail to activate so action can be taken before they are lost.
