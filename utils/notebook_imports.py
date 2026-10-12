"""Shared third-party and standard-library imports for project notebooks."""

import os
import pickle
import re
import warnings
from pathlib import Path

import joblib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import xgboost as xgb
import imblearn
from imblearn.over_sampling import SMOTE
from sklearn.calibration import calibration_curve
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    auc,
    average_precision_score,
    brier_score_loss,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

__all__ = [
    "ColumnTransformer",
    "OneHotEncoder",
    "Path",
    "Pipeline",
    "RandomForestClassifier",
    "SMOTE",
    "SimpleImputer",
    "StandardScaler",
    "accuracy_score",
    "auc",
    "average_precision_score",
    "brier_score_loss",
    "calibration_curve",
    "classification_report",
    "confusion_matrix",
    "f1_score",
    "imblearn",
    "joblib",
    "matplotlib",
    "np",
    "os",
    "pd",
    "pickle",
    "precision_recall_curve",
    "precision_score",
    "recall_score",
    "re",
    "roc_auc_score",
    "roc_curve",
    "sns",
    "sklearn",
    "train_test_split",
    "warnings",
    "xgb",
    "plt",
]
