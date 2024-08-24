import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Display data from the uploaded CSV
st.subheader("Solar Farm Data")
st.write(data.head())  # Display the first few rows of the data

# Display line charts for GHI, DNI, and DHI
st.subheader("Solar Radiation Components Over Time")
st.line_chart(data[['GHI', 'DNI', 'DHI']])

# Generate random data for a simple plot (example)
st.subheader("Random Data Histogram")
random_data = np.random.randn(1000)
hist_values = np.histogram(random_data, bins=30)[0]
st.bar_chart(hist_values)

# Simple line chart example with random data
st.subheader("Line Chart Example")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Simple Matplotlib plot
st.subheader("Matplotlib Example")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title("Matplotlib Line Plot")
ax.legend()
st.pyplot(fig)

# Final message
st.write("Thank you for using the Solar Farm Data Dashboard!")
