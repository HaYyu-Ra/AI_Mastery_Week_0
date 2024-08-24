import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the Streamlit app
st.title('Solar Farm Data Dashboard')

# Path to your Excel data
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\pythonapp\data\solar_farm_data.csv'

# Load the data from Excel
data = pd.read_excel(file_path)

# Display basic information about the dataset
st.sidebar.header('Dataset Information')
st.sidebar.write(f"Number of rows: {data.shape[0]}")
st.sidebar.write(f"Number of columns: {data.shape[1]}")
st.sidebar.write(f"Columns: {', '.join(data.columns)}")

# Select columns to display in the line chart
st.sidebar.header('Select Columns for Line Chart')
columns = st.sidebar.multiselect('Columns', data.columns, default=['GHI', 'DNI', 'DHI'])

# Display a line chart with selected columns
st.subheader('Line Chart')
st.line_chart(data[columns])

# Add a histogram for GHI
st.sidebar.header('GHI Histogram')
if 'GHI' in data.columns:
    st.sidebar.subheader('GHI Histogram')
    bins = st.sidebar.slider('Number of bins', min_value=10, max_value=100, value=20)
    
    fig, ax = plt.subplots()
    ax.hist(data['GHI'].dropna(), bins=bins, edgecolor='black')
    ax.set_title('Histogram of GHI')
    ax.set_xlabel('GHI')
    ax.set_ylabel('Frequency')
    st.sidebar.pyplot(fig)
else:
    st.sidebar.write("Column 'GHI' is not present in the dataset.")

# Add a summary statistics section
st.subheader('Summary Statistics')
st.write(data.describe())

# Add interactive filter for data
st.sidebar.header('Data Filtering')
start_date = st.sidebar.date_input('Start Date', value=data['Date'].min())
end_date = st.sidebar.date_input('End Date', value=data['Date'].max())

filtered_data = data[(data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <= pd.to_datetime(end_date))]

st.subheader('Filtered Data')
st.write(filtered_data)
