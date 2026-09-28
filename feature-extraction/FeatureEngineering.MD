# Feature Engineering Guide

## Overview

This document summarises the feature engineering stage of the CAP182 project. Feature engineering transforms the cleaned dataset into meaningful variables that improve model learning and predictive power.

## Related notebook

- [feature-extraction/02_Feature_Engineering.ipynb](feature-extraction/02_Feature_Engineering.ipynb)

## What the notebook does

The notebook focuses on creating high-value customer and behavioural features such as:

- recency, frequency, and monetary values
- customer lifecycle measures
- engagement and spending behaviour indicators
- derived temporal variables for predictive modelling
- final engineered feature sets for model training

## How to use the notebook

1. Open the feature engineering notebook.
2. Ensure the cleaned dataset from preprocessing is available.
3. Run each cell sequentially to generate the engineered features.
4. Verify the output tables and feature set before using them in model training.
5. Export the final engineered dataset for the modelling stage.

## Expected output

The notebook produces engineered features and prepared training/test data that can be used in the Random Forest and XGBoost model workflows.
