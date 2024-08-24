import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Correct path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\solar_farm_data.xlsx'

# Check if the file exists and load the data
try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"Error: The file at {file_path} does not exist.")
    exit()

# Calculate correlation matrix
correlation = df.corr()

# Plot correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')

# Save the plot to a file
output_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\correlation_heatmap.png'
plt.savefig(output_path)

# Show the plot
plt.show()
