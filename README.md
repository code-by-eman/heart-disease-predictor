# Heart Disease Risk Predictor

A small Streamlit app that takes four health numbers and predicts whether heart disease is likely present. The model behind it is a Support Vector Classifier trained on the UCI Cleveland heart disease data.

## What the app asks for

| Input | Meaning |
|---|---|
| Age | Age in years |
| Resting Blood Pressure | mm Hg |
| Serum Cholesterol | mg/dl |
| Maximum Heart Rate | Highest heart rate reached |

It answers with one of two results:

- `0`: no heart disease
- `1`: heart disease present

All four inputs are plain numbers, so nothing needs encoding.

## Setup

1. Download the Cleveland processed data file from the [UCI Heart Disease page](https://archive.ics.uci.edu/dataset/45/heart+disease).
2. Rename it to `processed.cleveland.data` and put it in this folder.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Build the model

Open the notebook and run every cell from top to bottom:

```bash
jupyter notebook
```

Running `Heart_Disease_ML.ipynb` creates these files:

- `heart_disease.csv`: the cleaned data (4 inputs + the result)
- `training-data.csv` and `testing-data.csv`: the 80/20 split
- `model-predictions.csv`: the model's guesses on the test rows
- `heart_disease_model.pkl`: the trained model that the app loads

## Run the app

```bash
streamlit run app.py
```

## Deploying on Streamlit Community Cloud

Push these files to a GitHub repository, then deploy `app.py` from it:

- `app.py`
- `requirements.txt`
- `heart_disease_model.pkl`

The notebook and CSV files are optional extras.

## Data source

UCI Machine Learning Repository, Heart Disease (Cleveland processed data).

## Disclaimer

This is a learning project. It is not a medical tool and should not be used to diagnose or treat anyone.
