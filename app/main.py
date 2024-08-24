import streamlit as st
import pandas as pd

st.title('Solar Farm Data Analysis')

# Load data
data_path = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/pythonapp/data/solar_data.xlsx"
df = pd.read_excel(data_path)

# Display data summary
st.write("Data Summary:")
st.write(df.describe())

# Plot line chart
st.line_chart(df[['GHI', 'DNI', 'DHI', 'Tamb']])
