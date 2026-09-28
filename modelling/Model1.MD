# Model 1 Guide

## Overview

This document describes the first predictive model used in the project: a Random Forest classifier.

## Related notebook

- [modelling/03_Model_1_Random_Forest.ipynb](modelling/03_Model_1_Random_Forest.ipynb)

## Model purpose

Model 1 is used to predict whether a customer will convert to an active investor based on the prepared dataset and engineered features.

## What the notebook does

- loads the cleaned and engineered dataset
- splits the data into training and testing sets
- configures a Random Forest classifier
- trains the model
- makes predictions on unseen data
- saves prediction outputs for later evaluation

## How to use the notebook

1. Open the notebook in Jupyter or VS Code.
2. Ensure the feature-engineered data is available.
3. Run the cells in order.
4. Check that the model trains successfully and outputs predictions.
5. Use the saved prediction files for evaluation and performance analysis.

## Expected output

The notebook produces model predictions and stores the generated output for use in the Model 1 performance assessment.
