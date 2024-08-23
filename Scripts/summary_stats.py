import pandas as pd

# Load the dataset
data_path = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/data/solar_data.xlsx"
df = pd.read_excel(data_path)

# Calculate summary statistics
summary = df.describe()
print(summary)
