import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('your_data.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot time series data for GHI, DNI, DHI
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['GHI'], label='GHI')
plt.plot(df['Date'], df['DNI'], label='DNI')
plt.plot(df['Date'], df['DHI'], label='DHI')

# Add labels and legend
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

# Show the plot
plt.show()
