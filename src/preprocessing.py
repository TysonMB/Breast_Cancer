import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from train import train_val_test


train_input, y_train, val_input, y_val, test_input, y_test = train_val_test()

def scaling_numeric_values():
    scaler = StandardScaler() #Creating a stamdard scaler object

    scaler.fit(train_input) #fitting tthe scaler object
    x_train = scaler.transform(train_input)
    x_val = scaler.transform(val_input)
    x_test = scaler.transform(test_input)

    return x_train, x_val, x_test


