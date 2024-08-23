import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\your_data.xlsx'

# Load your data from Excel
df = pd.read_excel(file_path)

# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot time series data
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['GHI'], label='GHI')
plt.plot(df['Date'], df['DNI'], label='DNI')
plt.plot(df['Date'], df['DHI'], label='DHI')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.title('Time Series Analysis')
plt.grid(True)
plt.show()
