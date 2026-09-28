# Model 2 Guide

## Overview

This document describes the second predictive model used in the project: an XGBoost classifier with an ensemble strategy.

## Related notebook

- [modelling/04_Model_2_XGBoost_Ensemble.ipynb](modelling/04_Model_2_XGBoost_Ensemble.ipynb)

## Model purpose

Model 2 is designed to improve classification performance by using a strong boosting model and ensemble-based prediction logic for account activation analysis.

## What the notebook does

- loads the cleaned and engineered dataset
- prepares training and testing samples
- configures XGBoost hyperparameters
- trains the model using the prepared features
- generates ensemble prediction outputs
- stores model outputs for comparison with Model 1

## How to use the notebook

1. Open the notebook in Jupyter or VS Code.
2. Confirm that the processed feature dataset is available.
3. Run the notebook from start to finish.
4. Check the model training logs and prediction outputs.
5. Use the saved predictions in the Model 2 performance notebook.

## Expected output

The notebook generates XGBoost and ensemble predictions for comparison and evaluation against Model 1.
