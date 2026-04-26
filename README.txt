# Breast Cancer Prediction App

- Project Overview

This project is a machine learning application that predicts whether a breast tumor is **benign** or **malignant** using clinical measurement features.

The system demonstrates an end-to-end production ML workflow including:

* Data preprocessing
* Feature selection
* Hyperparameter tuning using GridSearchCV
* Model deployment with Streamlit
* Schema validation and safe prediction pipeline


- Business Problem

Early detection of breast cancer significantly improves survival rates.
This application assists healthcare practitioners by providing an ML-powered risk prediction based on tumor characteristics.


- Machine Learning Pipeline

The model was developed using a **production-style pipeline**:

1. Data cleaning and preprocessing
2. Feature scaling using StandardScaler
3. Feature selection
4. Hyperparameter optimization with GridSearchCV
5. Final model training
6. Model artifact saving (`model.pkl`)
7. Metadata & schema validation

- Model Used

* RandomForestClassifier (best estimator from GridSearchCV)


- Project Structure

breast_cancer_ml/
│
├── data/                   # Dataset files
│   __ data.csv
│
│
│── models/                 # Saved ML artifacts
│   ── model.pkl
│   ── metadata.json
│   __ metrics.json
│   __ features.jason
│
│
│   
├── src/
│   ── about.py             # About the app
│   ── predict_page.py      # Streamlit UI 
│             
│
│__ ml/
│   __ predict.py           # Prediction pipeline service
│   __ preprocessing.py     # Feature validation 
│   __ train.py             # Training 
│
│
├── app/
│   ── app.py
│ 
│
├── notebook/               # notebook from jupyternotebook
│   ── Breast_Cancer Final.ipynb
│
├── requirements.txt
└── README.md


- Installation

Clone the repository:

git clone <your-repo-link>
cd breast_cancer_ml


Create environment:

conda create -n breast_cancer python=3.10
conda activate breast_cancer


Install dependencies:

pip install -r requirements.txt

- Run Streamlit Application

streamlit run app/app.py

Open browser:

http://localhost:8501

- Prediction Workflow

User Input → Schema Validation → ML Pipeline → Prediction Output


- Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Streamlit
* Joblib


- Future Improvements

* REST API deployment with FastAPI
* Docker containerization
* Cloud deployment
* Model monitoring & drift detection


- Author

Tyson Muchinzi
Soon To Be Machine Learning Engineer
