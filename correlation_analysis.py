import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to your Excel data
file_path = 'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\solar_farm_data.csv'

# Load your data from Excel
df = pd.read_excel(file_path)

# Calculate correlation matrix
correlation = df.corr()

# Plot correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()
