import numpy as np
import pandas as pd
import pickle
import joblib
import json
from sklearn.ensemble import RandomForestClassifier 
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from preprocessing import scaling_numeric_values,  y_train, y_val, y_test


x_train, x_val, x_test = scaling_numeric_values()


def rf_pipeline():
    #Grid Search using Random Forest Regressor
    pipline = Pipeline(steps =[
        ('feature_selectors', SelectKBest(score_func = f_classif, k =3)),
        ('rf_model', RandomForestClassifier(bootstrap=False, min_samples_split =5, n_estimators = 8, max_depth = 3, max_leaf_nodes = 10))
        ])
    
    para_grim = {
        'feature_selectors__k': [3],
        'rf_model__n_estimators': [10],
        'rf_model__max_depth': [3],
        'rf_model__max_leaf_nodes': [8],
        'rf_model__min_samples_split': [2]
        
    }

    return pipline, para_grim

pipline, para_grim = rf_pipeline()

def grid_search():
    grid_search = GridSearchCV(
        estimator = pipline,
        param_grid = para_grim,
        cv = 10,
        scoring = 'recall',
        n_jobs = -1,
        refit = True,
        return_train_score = True
    ) 

    #fitting the grid search for the random forest
    grid_search.fit(x_train, y_train)

    #printing the best parameters and the cross_validation_score
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Best CV Score: {grid_search.best_score_:,.2f}")

    #Getting the classification report of the grid search
    best_model = grid_search.best_estimator_
    y_predict_best = best_model.predict(x_val)
    val_score = classification_report(y_val, y_predict_best)

    print(f"THE VAL SCORE IS:")
    print(val_score)

grid_search()