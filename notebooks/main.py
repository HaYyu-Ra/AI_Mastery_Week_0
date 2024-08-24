import streamlit as st
import pandas as pd

st.title('Solar Farm Data Dashboard')

# Load the solar farm data
data_path = 'C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/data/solar_farm_data.csv'
data = pd.read_csv(data_path)

# Display line chart for GHI, DNI, and DHI
st.line_chart(data[['GHI', 'DNI', 'DHI']])
