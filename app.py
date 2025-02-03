# Imports
import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file into a DataFrame
project_data = pd.read_csv("vehicles_us.csv")

# Convert to datetime
project_data['date_posted'] = pd.to_datetime(project_data['date_posted'])

# Fill missing values
project_data['model_year'] = project_data['model_year'].fillna(project_data['model_year'].median())
project_data['cylinders'] = project_data.groupby('model')['cylinders'].fillna(project_data['cylinders'].median())
project_data['odometer'] = project_data.groupby('model')['odometer'].fillna(project_data['odometer'].median())
project_data['paint_color'].fillna('unknown', inplace=True)
project_data.info()

st.header('Vehicle Data Analysis')

# Filter data
filtered_data = project_data[project_data['price'] > 0]

# plot histogram
prices = px.histogram(
    filtered_data,
    x='price',
    nbins=50, 
    title='Distribution of Vehicle Prices',
    labels=('Number of Vehicles', 'Price')
)
prices.update_layout(xaxis_title='Price', yaxis_title='Number of Vehicles')
st.plotly_chart(prices)

# Summary
st.write("""
         ### Summary:
Price data reveals a wide range of vehicle prices, from 1 to 375,000, with a mean of 12,160 and a median of 9,000, indicating a right-skewed distribution. The interquartile range (IQR) spans from 5,000 to 16,900, showing most vehicles are priced moderately. The high standard deviation of 10,082 highlights significant variability in pricing. These findings suggest that while some high-priced vehicles skew the average, the majority are more affordable, presenting opportunities for targeted pricing strategies and customer segmentation.
         """)

# Filter the data
filtered_data = project_data[project_data['price'] > 0]

# plot scatter
price_odometer = px.scatter(
    filtered_data,
    x='odometer',
    y='price',
    title='Price vs Odometer'
)
price_odometer.update_layout(xaxis_title='Odometer Reading', yaxis_title='Price')
st.plotly_chart(price_odometer)

# Summary
st.write("""
         ### Summary:
The scatter plot of price versus odometer reading shows a general trend where vehicles with higher odometer readings tend to have lower prices, which aligns with the expectation that higher mileage often correlates with decreased vehicle value. However, there are outliers, with some high-mileage vehicles still priced significantly higher than the majority, suggesting other factors influencing the price. This pattern can inform pricing strategies, where higher-mileage vehicles might need adjustments or incentives to remain competitive in the market. Additionally, the presence of outliers indicates that while mileage is important, other vehicle attributes, such as condition or brand, may also be playing a substantial role in determining price.
         """)
