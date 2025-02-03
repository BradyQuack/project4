# Imports
import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file into a DataFrame
project_data = pd.read_csv("C:/Users/brady/OneDrive/Desktop/PythonEnv/project4/vehicles_us.csv")

st.header('Vehicle Price and Model Year Analysis')
price_histogram = px.histogram(project_data, x='price', nbins=50, title='Distribution of Vehicle Prices')
st.plotly_chart(price_histogram)

# Filter the data
filtered_data = project_data[(project_data['price'] > 0) & (project_data['odometer'] > 0)]

# Plot a scatter plot for Price vs Odometer
price_odometer = px.scatter(
    filtered_data,
    x='odometer',
    y='price',
    title='Price vs Odometer'
)
st.plotly_chart(price_odometer)

# Add checkbox for scatter plot
show_scatter = st.checkbox('Show Price vs Odometer Scatter Plot')
if show_scatter:
    st.plotly_chart(price_odometer)

# Add checkbox for price histogram
show_histogram = st.checkbox('Show Price Distribution Histogram')
if show_histogram:
    st.plotly_chart(price_histogram)