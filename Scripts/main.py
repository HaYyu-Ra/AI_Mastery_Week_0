import streamlit as st
import pandas as pd

# Set the title of the Streamlit app
st.title('Solar Farm Data Dashboard')

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\your_data.xlsx'

# Load the data from Excel
data = pd.read_excel(file_path)

# Display a line chart with GHI, DNI, and DHI
st.line_chart(data[['GHI', 'DNI', 'DHI']])
