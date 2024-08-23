import streamlit as st
import pandas as pd

st.title('Solar Farm Data Dashboard')

# Load the data
data = pd.read_csv('C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/path/to/your/solar_farm_data.csv')

# Display a line chart
st.line_chart(data[['GHI', 'DNI', 'DHI']])
