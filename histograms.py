import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\your_data.xlsx'

# Load your data from Excel
df = pd.read_excel(file_path)

# Histogram for GHI
plt.figure(figsize=(10, 5))
df['GHI'].hist(bins=30)
plt.xlabel('GHI')
plt.ylabel('Frequency')
plt.title('Histogram of GHI')
plt.grid(True)
plt.show()
