import pandas as pd
from scipy import stats
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

def inspect_data(data):
    print(data.head())
    print(data.info())
    print(data.describe())

def data_quality_check(data):
    missing_values = data.isnull().sum()
    print(missing_values)
    
    z_scores = stats.zscore(data.select_dtypes(include=['float64', 'int64']))
    abs_z_scores = np.abs(z_scores)
    outliers = (abs_z_scores > 3).all(axis=1)
    return missing_values, outliers

def summary_statistics(data):
    return data.describe()
