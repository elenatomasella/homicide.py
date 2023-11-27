import pandas as pd
import altair as alt

# Load the dataset
homicide_df = pd.read_csv("database.csv", low_memory=False)

# Aggregate data by state
statewise_counts = homicide_df['State'].value_counts().reset_index()
statewise_counts.columns = ['State', 'Number of Homicides']

# Create a bar chart with different colors for each state
statewise_chart = alt.Chart(statewise_counts).mark_bar().encode(
    x='Number of Homicides',
    y=alt.Y('State', sort='-x'),
    color='State:N'  # Assign a unique color to each state
).properties(
    title='State Distribution of Homicides',
    width=900,
    height=700
).configure_title(
    font='sans',
    fontSize=14,
    color='navy'
).configure_view(
    strokeWidth=0
).configure_axis(
    labelFont='sans',
    labelFontSize=14,
    labelColor='navy',
    titleFont='sans',
    titleFontSize=14,
    titleColor='navy',
    gridColor='lightgray'
)

statewise_chart.save('statewise_distribution.html')


import pandas as pd
import plotly.express as px

# Load the homicide dataset
homicide_df = pd.read_csv('database.csv', low_memory=False)
# Dictionary to map full state names to two-letter abbreviations
state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
    'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
    'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

# Convert full state names to abbreviations in your dataset
homicide_df['State'] = homicide_df['State'].map(state_abbreviations)

# Then, proceed with the aggregation and plotting as before
statewise_counts = homicide_df['State'].value_counts().reset_index()
statewise_counts.columns = ['State', 'Number of Homicides']

# Create a choropleth map using Plotly
fig = px.choropleth(statewise_counts,
                    locations='State',
                    locationmode='USA-states',
                    color='Number of Homicides',
                    scope='usa',
                    title='Heatmap of Homicides in the USA',
                    color_continuous_scale='Reds')

# Show the plot
fig.show()
