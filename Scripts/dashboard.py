import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title('Dashboard Example')

# Upload data file
uploaded_file = st.file_uploader("Upload your data file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Determine the file type and read the data accordingly
    if uploaded_file.name.endswith('csv'):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    # Display the data
    st.write("### Data Overview")
    st.write(data.head())

    # Display summary statistics
    st.write("### Summary Statistics")
    st.write(data.describe())

    # Histogram for a selected column
    st.write("### Histogram")
    column = st.selectbox("Select column for histogram", data.columns)
    if column:
        st.write(f"Histogram of {column}")
        fig, ax = plt.subplots()
        ax.hist(data[column].dropna(), bins=30)
        st.pyplot(fig)

    # Time Series Analysis (assuming there is a DateTime column)
    st.write("### Time Series Analysis")
    if 'DateTime' in data.columns:
        data['DateTime'] = pd.to_datetime(data['DateTime'])
        data.set_index('DateTime', inplace=True)
        st.line_chart(data['Value'])  # Replace 'Value' with your time series data column

else:
    st.write("Upload a file to see the data.")
