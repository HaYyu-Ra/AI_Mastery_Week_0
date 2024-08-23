import pandas as pd

# Load your data
df = pd.read_csv('your_data.csv')

# Calculate summary statistics
summary_stats = df.describe()

# Print summary statistics
print(summary_stats)
