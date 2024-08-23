import streamlit as st
import pandas as pd

st.title('Solar Farm Data Dashboard')

data = pd.read_csv('path/to/your/solar_farm_data.csv')
st.line_chart(data[['GHI', 'DNI', 'DHI']])
