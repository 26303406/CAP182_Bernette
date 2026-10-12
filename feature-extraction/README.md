# Feature Extraction

This folder contains the feature engineering workflow used to transform the cleaned dataset into model-ready inputs.

## Related notebook

- 02_Feature_Engineering.ipynb

## Purpose

Feature engineering creates meaningful customer and behavioural variables, such as recency, frequency, monetary value, engagement patterns, and transformation-based predictors that help improve model performance.

## What this notebook does

- loads the cleaned dataset from preprocessing
- creates new features from transaction and customer behaviour
- derives activity, spending, and engagement indicators
- prepares the final feature set for modelling
- exports the engineered dataset for training and evaluation

## How to use it

1. Open 02_Feature_Engineering.ipynb in VS Code or Jupyter.
2. Ensure the cleaned data generated in preprocessing is available.
3. Run the notebook cells in order from top to bottom.
4. Review the generated feature tables and shape checks.
5. Save the final engineered dataset for the modelling stage.

## Output

The notebook produces the engineered feature dataset used by the Random Forest and XGBoost models.
