import pandas as pd
import numpy as np

# Sample data
data = {
    'Temperature': [25, 30, 28, 22, 27, 29, 31, 26, 24, 23, np.nan],
    'Relative_Humidity': [55, 60, 58, 52, 57, 59, 61, 56, 54, 53, 60],
    'Solar_Radiation': [200, 250, 230, 180, 220, 240, 260, 210, 190, 185, 250]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data Quality Checks
def data_quality_checks(df):
    print("Data Quality Report")
    print("===================")
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Check for duplicate rows
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
    
    # Check for outliers using Z-score
    print("\nOutliers:")
    z_scores = np.abs((df - df.mean()) / df.std())
    outliers = (z_scores > 3).sum()
    print(outliers)
    
    # Summary statistics
    print("\nSummary Statistics:")
    print(df.describe())

# Run data quality checks
data_quality_checks(df)
