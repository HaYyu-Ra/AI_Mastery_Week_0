import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Temperature': [25, 30, 28, 22, 27, 29, 31, 26, 24, 23],
    'Relative_Humidity': [55, 60, 58, 52, 57, 59, 61, 56, 54, 53],
    'Solar_Radiation': [200, 250, 230, 180, 220, 240, 260, 210, 190, 185]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Scatter plot: Temperature vs. Relative Humidity
plt.figure(figsize=(10, 5))
plt.scatter(df['Relative_Humidity'], df['Temperature'], color='blue')
plt.title('Temperature vs. Relative Humidity')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Scatter plot: Temperature vs. Solar Radiation
plt.figure(figsize=(10, 5))
plt.scatter(df['Solar_Radiation'], df['Temperature'], color='green')
plt.title('Temperature vs. Solar Radiation')
plt.xlabel('Solar Radiation (W/m²)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Scatter plot: Relative Humidity vs. Solar Radiation
plt.figure(figsize=(10, 5))
plt.scatter(df['Relative_Humidity'], df['Solar_Radiation'], color='red')
plt.title('Relative Humidity vs. Solar Radiation')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Solar Radiation (W/m²)')
plt.grid(True)
plt.show()
