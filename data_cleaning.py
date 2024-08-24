import pandas as pd

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\solar_farm_data.csv'

# Load your data from Excel
df = pd.read_excel(file_path)

# Handling missing values
df = df.dropna()  # Remove rows with missing values
# df = df.fillna(method='ffill')  # Optionally fill missing values

# Remove or handle anomalies (example: removing outliers based on GHI)
df = df[df['GHI'] < df['GHI'].quantile(0.95)]  # Removing top 5% of GHI values

# Save cleaned data to a new file (optional)
df.to_excel(r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\cleaned_data.xlsx', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_data.xlsx'.")
