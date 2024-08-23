import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Temperature': [25, 30, 28, 22, 27, 29, 31, 26, 24, 23],
    'Relative_Humidity': [55, 60, 58, 52, 57, 59, 61, 56, 54, 53],
    'Solar_Radiation': [200, 250, 230, 180, 220, 240, 260, 210, 190, 185]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Print the correlation matrix
print(correlation_matrix)

# Visualize the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Scatter plot: Temperature vs. Relative Humidity
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Relative_Humidity', y='Temperature', data=df)
plt.title('Temperature vs. Relative Humidity')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Scatter plot: Temperature vs. Solar Radiation
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Solar_Radiation', y='Temperature', data=df)
plt.title('Temperature vs. Solar Radiation')
plt.xlabel('Solar Radiation (W/m²)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Scatter plot: Relative Humidity vs. Solar Radiation
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Relative_Humidity', y='Solar_Radiation', data=df)
plt.title('Relative Humidity vs. Solar Radiation')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Solar Radiation (W/m²)')
plt.grid(True)
plt.show()
