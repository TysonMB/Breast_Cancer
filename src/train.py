import numpy as np
import pandas as pd


#Loading the dataset
data_f = pd.read_csv('data.csv')

#Viewing the dataset and it's information
def dataset_overview():
    print('*' * 100)
    print('The first 5 rows of th dataset:')
    print(data_f.head(5))
    print('*' * 100)
    print('Shape of th dataset:')
    print(data_f.shape)
    print('*' * 105)
    print('Columns of the dataset:')
    print(data_f.columns)
    print('*' * 105)
    print('Information of the dataset:')
    print(data_f.info())
    print('*' * 105)
    print('Details of the dataset:')
    print(data_f.describe())

def new_dataset(data):
    new_data = data[['diagnosis', 'concave_points_mean', 'perimeter_worst', 'concave_points_worst']]
    new_data['diagnosis'] = (new_data['diagnosis'] == 'M').astype(int)#changing categorical data in to 1's and 0's
    
    return new_data

dataset = new_dataset(data_f)

def train_val_test():
    #splitting the data into trainning, validation and testing
    train, val, test = np.split(dataset.sample(frac = 1), [int(0.6 * len(dataset)), int(0.8 * len(dataset))]) 

    #Splitting the dataset into x and y
    y_train = train['diagnosis']
    train_input = train.drop(['diagnosis'], axis = 1)
    y_val = val['diagnosis']
    val_input = val.drop(['diagnosis'], axis = 1)
    y_test = test['diagnosis']
    test_input = test.drop(['diagnosis'], axis = 1)

    return train_input, y_train, val_input, y_val, test_input, y_test



