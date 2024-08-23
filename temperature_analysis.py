import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\your_data.xlsx'

# Load your data from Excel
df = pd.read_excel(file_path)

# Scatter plot for Temperature Analysis
plt.figure(figsize=(10, 5))
plt.scatter(df['RH'], df['Tamb'])
plt.xlabel('Relative Humidity')
plt.ylabel('Temperature')
plt.title('Temperature vs Relative Humidity')
plt.grid(True)
plt.show()
