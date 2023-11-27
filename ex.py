import pandas as pd
import plotly.express as px

# Load the homicide dataset
homicide_df = pd.read_csv('database.csv', low_memory=False)

# Load the city coordinates dataset
city_coords_df = pd.read_csv('us_cities.csv', low_memory=False)

# Merge the datasets on city names
merged_df = pd.merge(homicide_df, city_coords_df, left_on='City', right_on='CITY', how='left')

# Aggregate data by city
citywise_counts = merged_df.groupby(['CITY', 'LATITUDE', 'LONGITUDE']).size().reset_index(name='Number of Homicides')

# Filter out rows with missing values (cities that couldn't be matched)
citywise_counts.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)

# Create a scatter plot using Plotly
fig = px.scatter_geo(citywise_counts,
                     lat='LATITUDE',
                     lon='LONGITUDE',
                     size='Number of Homicides',
                     hover_name='CITY',
                     scope="usa",
                     title='City-wise Distribution of Homicides in the USA')

# Update layout for font customization
fig.update_layout(
    title_font=dict(family='sans', size=14, color='navy'),
    font=dict(family='sans', size=14, color='navy')
)

# Show the plot
fig.show()
