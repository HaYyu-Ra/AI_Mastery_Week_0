import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the web app
st.title("Solar Farm Data Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name:", "User")
user_age = st.sidebar.slider("Select your age:", 0, 100, 25)

# Display user input
st.write(f"Hello, {user_name}!")
st.write(f"You are {user_age} years old.")

# Path to the data
data_path = 'data/solar_farm_data.csv'  # Ensure this file path matches your actual data file

# Load the data
df = pd.read_csv(data_path)

# Display the contents of the data file
st.subheader("Loaded Solar Farm Data")
st.write(df)

# Summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Line chart for GHI, DNI, DHI
st.subheader("Solar Radiation Over Time")
st.line_chart(df[['GHI', 'DNI', 'DHI']])

# Histogram for Temperature and Wind Speed
st.subheader("Histograms of Temperature and Wind Speed")
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].hist(df['Tamb'].dropna(), bins=30, color='orange', alpha=0.7)
ax[0].set_title("Ambient Temperature (Tamb) Histogram")
ax[0].set_xlabel("Temperature (°C)")
ax[0].set_ylabel("Frequency")

ax[1].hist(df['WS'].dropna(), bins=30, color='blue', alpha=0.7)
ax[1].set_title("Wind Speed (WS) Histogram")
ax[1].set_xlabel("Wind Speed (m/s)")
ax[1].set_ylabel("Frequency")

st.pyplot(fig)

# Correlation heatmap
st.subheader("Correlation Heatmap")
correlation_matrix = df[['GHI', 'DNI', 'DHI', 'Tamb', 'WS', 'RH']].corr()

fig, ax = plt.subplots()
cax = ax.matshow(correlation_matrix, cmap='coolwarm')
fig.colorbar(cax)
ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha='left')
ax.set_yticklabels(correlation_matrix.columns)
ax.set_title("Correlation Heatmap")

st.pyplot(fig)

# Z-Score Analysis
st.subheader("Z-Score Analysis")
z_scores = (df[['GHI', 'DNI', 'DHI']] - df[['GHI', 'DNI', 'DHI']].mean()) / df[['GHI', 'DNI', 'DHI']].std()
st.write(z_scores)

# Final message
st.write("Thank you for using the Solar Farm Data Dashboard!")
