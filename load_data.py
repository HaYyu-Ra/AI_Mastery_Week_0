import pandas as pd

# Define the data path
data_path = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/data/solar_data.xlsx"

# Load the data
df = pd.read_excel(data_path)

# Display the first few rows of the dataframe
print(df.head())
