import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\your_data.xlsx'

# Load your data from Excel
df = pd.read_excel(file_path)

# Plot Wind Speed over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['WindSpeed'], label='Wind Speed')
plt.xlabel('Date')
plt.ylabel('Wind Speed')
plt.title('Wind Speed Over Time')
plt.legend()
plt.grid(True)
plt.show()

# If you have wind direction data, you can also plot it
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['WindDirection'], label='Wind Direction', color='orange')
plt.xlabel('Date')
plt.ylabel('Wind Direction')
plt.title('Wind Direction Over Time')
plt.legend()
plt.grid(True)
plt.show()
