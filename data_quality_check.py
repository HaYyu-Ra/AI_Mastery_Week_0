import pandas as pd

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\your_data.xlsx'

# Load your data from Excel
df = pd.read_excel(file_path)

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Detect outliers using IQR method
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Define outliers as data points outside the range (Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)
outliers = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))
print("\nOutliers detected using IQR method:")
print(outliers.sum())
