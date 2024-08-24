import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the web app
st.title("Solar Farm Data Dashboard")

# Path to your data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\solar_farm_data.xlsx'

# Load the data
@st.cache
def load_data():
    return pd.read_excel(file_path)

df = load_data()

# Display the dataframe
st.subheader("Uploaded CSV File")
st.write(df)

# Calculate correlation matrix
correlation = df.corr()

# Plot correlation heatmap
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
st.pyplot(plt)
