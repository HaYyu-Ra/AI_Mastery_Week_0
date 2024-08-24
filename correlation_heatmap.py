import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Title of the web app
st.title("Solar Farm Data Dashboard")

# Path to your data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\solar_farm_data.csv'

# Function to load the data
@st.cache_data
def load_data():
    if os.path.exists(file_path):
        try:
            # Attempt to read the CSV file
            return pd.read_csv(file_path)
        except ValueError as e:
            st.error(f"Error reading CSV file: {e}")
            return pd.DataFrame()
    else:
        st.error(f"File not found: {file_path}")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found

df = load_data()

if not df.empty:
    # Display the dataframe
    st.subheader("Uploaded Data")
    st.write(df)

    # Display data types of the columns
    st.subheader("Data Types")
    st.write(df.dtypes)

    # Filter only numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    if not numeric_df.empty:
        # Calculate correlation matrix
        correlation = numeric_df.corr()

        # Plot correlation heatmap
        st.subheader("Correlation Heatmap")
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Heatmap')
        st.pyplot(plt)
    else:
        st.write("No numeric columns available for correlation analysis.")
else:
    st.write("Please upload the data file to see the results.")
