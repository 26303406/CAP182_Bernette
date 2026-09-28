# Preprocessing Guide

## Overview

This document describes the preprocessing stage of the CAP182 project. The preprocessing work prepares the raw retail transaction dataset for downstream modelling and feature engineering.

## Related notebook

- [preprocessing/01_Data_Preprocessing.ipynb](preprocessing/01_Data_Preprocessing.ipynb)

## What the notebook does

The notebook covers the following steps:

- loading the raw UCI Online Retail II dataset
- checking data structure and schema
- identifying missing values and invalid records
- removing duplicate transactions
- removing non-positive or invalid quantities and prices
- converting date fields to datetime format
- creating a reliable reference date for recency calculations
- aggregating transaction-level data into customer-level features
- preparing the cleaned dataset for feature extraction and modelling

## How to use the notebook

1. Open the notebook in Jupyter or VS Code.
2. Run the cells in order from top to bottom.
3. Confirm that the data loads correctly and the output summary matches the expected record counts.
4. Review the cleaned dataset before proceeding to feature engineering.
5. Save the processed dataset for use in the next project stage.

## Expected output

The preprocessing stage produces a cleaned transactional or customer-level dataset that is suitable for feature engineering, model training, and performance evaluation.
