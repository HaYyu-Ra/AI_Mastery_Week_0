import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the web app
st.title("Solar Farm Data Dashboard")

# Load the data from the local path
data_path = 'C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/data/solar_farm_data.csv'
data = pd.read_csv(data_path)

# Sidebar for user input
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name:", "User")
user_age = st.sidebar.slider("Select your age:", 0, 100, 25)

# Display user input
st.write(f"Hello, {user_name}!")
st.write(f"You are {user_age} years old.")

# Display data from the CSV
st.subheader("Solar Farm Data Overview")
st.write(data.head())  # Display the first few rows of the data

# Display line charts for GHI, DNI, and DHI
st.subheader("Solar Radiation Components Over Time")
st.line_chart(data[['GHI', 'DNI', 'DHI']])

# Summary Statistics
st.subheader("Summary Statistics")
st.write(data.describe())

# Data Quality Check
st.subheader("Data Quality Check")
missing_values = data.isnull().sum()
st.write("Missing Values in Each Column:")
st.write(missing_values)

# Histogram of GHI, DNI, and DHI
st.subheader("Histograms of Solar Radiation Components")
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
data['GHI'].hist(ax=ax[0], bins=30, color='blue')
ax[0].set_title('GHI Distribution')
data['DNI'].hist(ax=ax[1], bins=30, color='green')
ax[1].set_title('DNI Distribution')
data['DHI'].hist(ax=ax[2], bins=30, color='red')
ax[2].set_title('DHI Distribution')
st.pyplot(fig)

# Time Series Analysis
st.subheader("Time Series Analysis")
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data.set_index('Timestamp', inplace=True)
st.line_chart(data[['GHI', 'DNI', 'DHI']])

# Correlation Analysis
st.subheader("Correlation Analysis")
corr = data[['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB']].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Wind Analysis
st.subheader("Wind Analysis")
fig, ax = plt.subplots(figsize=(8, 6))
ax = plt.subplot(111, polar=True)
wind_speeds = data['WS']
wind_dirs = np.deg2rad(data['WD'])
ax.scatter(wind_dirs, wind_speeds, c=wind_speeds, cmap='viridis', alpha=0.75)
ax.set_title('Wind Speed and Direction')
st.pyplot(fig)

# Temperature Analysis
st.subheader("Temperature Analysis")
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(data['RH'], data['Tamb'], c='blue', alpha=0.5)
ax.set_xlabel('Relative Humidity (%)')
ax.set_ylabel('Ambient Temperature (°C)')
ax.set_title('Temperature vs Relative Humidity')
st.pyplot(fig)

# Z-Score Analysis
st.subheader("Z-Score Analysis")
from scipy import stats
data_zscore = data[['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB']].apply(lambda x: stats.zscore(x, nan_policy='omit'))
st.write(data_zscore.head())

# Bubble Chart
st.subheader("Bubble Chart")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(data['GHI'], data['Tamb'], s=data['RH']*10, c=data['BP'], cmap='coolwarm', alpha=0.5)
ax.set_xlabel('GHI (W/m²)')
ax.set_ylabel('Ambient Temperature (°C)')
ax.set_title('GHI vs Ambient Temperature vs Relative Humidity')
st.pyplot(fig)

# Final message
st.write("Thank you for using the Solar Farm Data Dashboard!")
