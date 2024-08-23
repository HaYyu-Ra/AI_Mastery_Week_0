import pandas as pd
from scipy.stats import zscore

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\your_data.xlsx'

# Load your data from Excel
df = pd.read_excel(file_path)

# Z-Score Analysis
df['zscore_GHI'] = zscore(df['GHI'])
outliers = df[df['zscore_GHI'].abs() > 3]
print("Outliers based on Z-Score:")
print(outliers)
