import pandas as pd

# Path to your Excel data
file_path = 'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\solar_farm_data.csv'

# Load your data from Excel
df = pd.read_excel(file_path)

# Calculate summary statistics
summary_stats = df.describe()

# Print summary statistics
print(summary_stats)
