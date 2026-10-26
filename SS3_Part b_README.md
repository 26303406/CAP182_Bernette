# SS3 Part B: Step-by-Step Guide

This guide explains how to set up, run, and publish the STADIOEquities account-activation analysis.

## 1. What the project does

The analysis predicts whether an account makes its first deposit within 90 days of registration:

- `activated = 1`: first deposit within 90 days
- `activated = 0`: no first deposit within 90 days

The notebook audits the client tables, prepares account-level features, trains and evaluates classification models, compares them statistically, and creates visualisations.

## 2. Files and folders

- `BernetteLesejane_26303406_CAP182_SS3_PartB.ipynb` - notebook with the repository-aware data path setup; use this notebook for the steps below.
- `data/` - the 12 source CSV tables.
- `artifacts/` - prepared datasets, split assignments, preprocessing objects, trained models, and predictions.
- `results/` - audit tables, metrics, comparisons, and evaluation outputs.
- `results/figures/` - saved plots.
- `requirements.txt` - Python dependencies for the project.

The repository also contains other Part B notebook copies. To avoid running a copy with different paths or stale outputs, use the notebook named above for this guide.

## 3. Prepare the environment

1. Clone or download the repository from GitHub.
2. Open the repository folder in VS Code.
3. Confirm that `data/` contains the 12 `table*.csv` files.
4. Open a terminal at the repository root and create a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   If PowerShell blocks virtual-environment activation, either follow your organisation's approved execution-policy guidance or run the environment's Python directly:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. In VS Code, open the notebook and select the `.venv` Python interpreter as its kernel.

## 4. Configure the data folder

The notebook searches the current working directory and its parent directories for:

```text
data/table01_registration_onboarding.csv
```

When it finds the repository, it uses that repository's `data/` folder. Start Jupyter or VS Code with the repository open so the notebook can locate it.

If the CSV files are stored somewhere else, set `SS3_DATA_DIR` to the directory containing them before starting VS Code or Jupyter. For example, in PowerShell:

```powershell
$env:SS3_DATA_DIR = "C:\path\to\CAP182_Bernette\data"
```

Replace the example path with the actual full path on your computer. If no data folder is found, the setup cell raises a `FileNotFoundError` with guidance.

## 5. Run the notebook

1. Open `BernetteLesejane_26303406_CAP182_SS3_PartB.ipynb`.
2. If the notebook has a package-install cell, let it finish. Restart the kernel only if the notebook or VS Code indicates that newly installed packages are not available.
3. Choose **Restart Kernel** and **Run All** if the kernel has old variables, or run the notebook cells from top to bottom in order.
4. Wait for each cell to finish. Resolve any errors before continuing; later cells depend on files and variables produced earlier.
5. Save the notebook after it completes. Saved cell outputs, including plots, are what GitHub displays in its notebook preview.

The main analysis sections run in this order:

1. **Dataset loading** - inventories the 12 tables, records relevance and leakage decisions, and audits data quality and target balance.
2. **Data preparation** - standardises categories, handles types and leakage, builds the modelling dataset, and creates train, validation, and test splits.
3. **Model training** - trains the project classifiers and saves models and predictions.
4. **Model validation** - evaluates performance across the data splits and performs sensitivity checks.
5. **Statistical model comparison** - compares cross-validation results and tests model differences.
6. **Results visualisation** - displays the charts and saves figure files.

## 6. Find the outputs

After a successful run, check:

- `results/01_dataset_summary.csv` and related `01_*.csv` files for the data audit.
- `artifacts/` for the prepared data, model files, and predictions.
- `results/03_*.csv`, `results/04_*.csv`, and `results/05_*.csv` for training, evaluation, and statistical comparison results.
- `results/figures/` for the saved visualisations.

The plotting cell should also display charts directly below it in the notebook. To show those charts on GitHub, save the notebook after the cell has run, then commit and push the notebook with its saved outputs.

## 7. Commit and push the completed notebook

Save the notebook in VS Code, then run these commands from the repository root. Stage only the files you intend to publish:

```powershell
git status
git add "BernetteLesejane_26303406_CAP182_SS3_PartB.ipynb"
git add "SS3_Part b_README.md"
git commit -m "Document SS3 Part B workflow"
git push
```

If you changed figures or result files and want them included, explicitly stage those files too. Review `git status` before committing so unrelated generated files are not included accidentally.

## 8. Important data-publishing check

The `data/` folder contains client-provided information. Before publishing or pushing data, account identifiers, notebook outputs, or generated prediction files, confirm that you are authorised to share them in the GitHub repository. If the repository is public or the data is restricted, use an approved anonymised or synthetic dataset and remove sensitive outputs before publishing.
