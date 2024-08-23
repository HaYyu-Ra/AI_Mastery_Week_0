import streamlit as st
import pandas as pd

st.title('Solar Farm Data Analysis')

# Load data
data_path = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/data/solar_data.xlsx"
df = pd.read_excel(data_path)

st.write(df.describe())
st.line_chart(df[['GHI', 'DNI', 'DHI', 'Tamb']])
