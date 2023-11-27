"""
Homicide Data Analysis Script

This script is designed to perform an extensive analysis on homicide data. It includes a variety of functions to process, analyze, and visualize data related to homicides. The script's primary focus is on examining trends and patterns in homicide cases across different states, with a particular emphasis on Texas and California. 

Key Features:
- Data Import: Loads homicide data and converts it to a pandas DataFrame.
- Data Overview: Provides descriptive statistics and general information about the dataset.
- Data Cleaning: Handles missing values, outliers, and transforms categorical variables.
- Population Trend Analysis: Compares population growth between Texas and California.
- Homicide Trends Analysis: Examines trends in homicide cases, including comparisons of capital cities and states.
- Racial and Age Demographics: Analyzes the racial demographics of victims and perpetrators, and trends in their ages.
- Crime Solution Analysis: Looks at trends in solved and unsolved homicide cases.
- Visualization: Generates a variety of plots, including histograms, line plots, and pie charts to visualize the findings.
- Data Visualization Saving: Saves key visualizations as HTML files for further use.

Each analysis and visualization function in the script is documented with a detailed docstring, explaining its purpose, parameters, and usage. 

To execute the script, ensure all required dependencies are installed and run the script from a Python environment. The main entry point of the script is the `main()` function, which orchestrates the execution of various analyses and visualizations.

Dependencies:
- pandas
- matplotlib
- seaborn
- numpy
- plotly
- altair

Note: This script is designed for educational and analytical purposes and should be used accordingly.

Author: Edoardo Bollati - Claudia Cortese - Elena Tomasella - Zhao Wei Zhu
Date of Creation:
Last modification:
"""


# import necessary libraries
import matplotlib
print(matplotlib.get_backend())
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import altair as alt
import pandas as pd
import seaborn as sns
import numpy as np
import plotly.express as px
import tabulate as tbl


def plot_victim_age_trend(data1, data2, data3, suf1, suf2, suf3):
    """
        Plots the trend of victims' ages over the years for three different datasets.

        This function takes three datasets and their respective suffixes for labeling,
        converts the 'Victim Age' column to numeric, groups the data by 'Year',
        and calculates the mean victim age. It then plots these trends using matplotlib.

        Parameters:
        - data1, data2, data3 (DataFrame): DataFrames containing homicide data.
        - suf1, suf2, suf3 (str): Suffixes for labeling the datasets in the plot.

        Returns:
        None; the function plots the trends and shows the matplotlib plot.
        """
    i, colors = 0, ['orchid', 'mediumaquamarine', 'cornflowerblue']
    for (data, suf) in [(data1, suf1), (data2, suf2), (data3, suf3)]:
        # Convert 'Victim Age' to numeric
        data['Victim Age'] = pd.to_numeric(data['Victim Age'], errors='coerce')
        # Group data by 'Year' and calculate median
        grouped_data = data.groupby('Year')['Victim Age'].agg(['mean']).reset_index()
        # .agg is used to use functions on each group identify by groupby
        plt.plot(grouped_data['Year'], grouped_data['mean'], marker='o', linestyle='-', color=colors[i],
                 label=f'Average Age in {suf}')
        i += 1
    # adding labels and title
    plt.xlabel('year', fontdict={'family': 'sans',
                                 'style': 'normal',
                                 'color': 'navy',
                                 'weight': 'normal',
                                 'size': 12})
    plt.ylabel('age', fontdict={'family': 'sans',
                                'style': 'normal',
                                'color': 'navy',
                                'weight': 'normal',
                                'size': 12})
    plt.title(f'Victim Age Through the Years', fontdict={'family': 'sans',
                                                         'style': 'normal',
                                                         'color': 'navy',
                                                         'weight': 'normal',
                                                         'size': 14})

    # Adding grid lines
    plt.grid(True, linestyle='--', alpha=0.7, color='navy')
    # add a legend
    plt.legend(labelcolor='navy')
    # show the plot
    plt.show()

def plot_perpetrator_age_trend(data1, data2, data3, suf1, suf2, suf3):
    """
        Plots the trend of perpetrators' ages over the years for three different datasets.

        Similar to `plot_victim_age_trend`, this function processes data for the age of perpetrators.
        It groups the data by 'Year', calculates the mean perpetrator age, and plots these trends.

        Parameters:
        - data1, data2, data3 (DataFrame): DataFrames containing homicide data.
        - suf1, suf2, suf3 (str): Suffixes for labeling the datasets in the plot.

        Returns:
        None; the function plots the trends and shows the matplotlib plot.
        """
    i, colors = 0, ['orchid', 'mediumaquamarine', 'cornflowerblue']
    for (data, suf) in [(data1, suf1), (data2, suf2), (data3, suf3)]:
        data['Perpetrator Age'] = pd.to_numeric(data['Perpetrator Age'], errors='coerce')
        """" Group the data by 'Year' and calculate mean """
        grouped_data = data.groupby('Year')['Perpetrator Age'].agg(['mean']).reset_index()
        # .agg is used to use functions on each group identify by groupby
        plt.plot(grouped_data['Year'], grouped_data['mean'], marker='o', linestyle='-', color=colors[i],
                 label=f'Average Age in {suf}')
        i += 1
    # adding labels and title
    plt.xlabel('year', fontdict={'family': 'sans',
                                 'style': 'normal',
                                 'color': 'navy',
                                 'weight': 'normal',
                                 'size': 12})
    plt.ylabel('age', fontdict={'family': 'sans',
                                'style': 'normal',
                                'color': 'navy',
                                'weight': 'normal',
                                'size': 12})
    plt.title(f'Perpetrator Age Through the Years in {suf}', fontdict={'family': 'sans',
                                                                       'style': 'normal',
                                                                       'color': 'navy',
                                                                       'weight': 'normal',
                                                                       'size': 14})
    # Adding grid lines
    plt.grid(True, linestyle='--', alpha=0.7, color='navy')
    # add a legend
    plt.legend(labelcolor='navy')
    # show the plot
    plt.show()

# EDA about victim race
def plot_victim_race(data, suf):
    """
        Plots the distribution of victim race for a given dataset.

        This function takes a homicide dataset and creates two pie charts: one including 'Unknown' race entries
        and the other excluding them. It visualizes the racial distribution of victims in the dataset.

        Parameters:
        - data (DataFrame): DataFrame containing homicide data.
        - suf (str): Suffix for labeling the dataset in the plot title.

        Returns:
        None; the function plots the racial distribution and shows the matplotlib plot.
        """
    # Plot the victim race distribution
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    palettes = ['BuPu', 'YlGn']
    for i, data1 in enumerate([data, data[data['Victim Race'] != 'Unknown']]):
        colors = sns.color_palette(palettes[i])
        victim_race_counts = data1['Victim Race'].value_counts()
        total_victims = len(data1)
        percentages = victim_race_counts / total_victims * 100  # Calculate percentages
        labels = victim_race_counts.index
        axs[i].pie(victim_race_counts, colors=colors, startangle=140)
        # Draw a white circle in the center for a "donut" chart effect
        axs[i].add_artist(plt.Circle((0, 0), 0.4, color='white'))
        # Create a legend inside the pie chart with percentages
        legend_labels = [f'{label}: {count} ({percentage:.1f}%)' for label, count, percentage in
                         zip(labels, victim_race_counts, percentages)]
        legend = axs[i].legend(legend_labels, title="Legend", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
                               labelcolor='navy')
        legend.get_title().set_color('navy')
    # Label title for the entire subplot
    axs[0].set_title('Considering unknown race', color='navy')
    axs[1].set_title('Dropping unknown race', color='navy')
    fig.suptitle(f'Victim Race distribution in {suf}', fontdict={'family': 'sans',
                                                                 'style': 'normal',
                                                                 'color': 'navy',
                                                                 'weight': 'normal',
                                                                 'size': 14})
    # Adjust layout to prevent overlapping
    plt.tight_layout()
    # Show the plot
    plt.show()

# EDA about perpetrator race
def plot_perpetrator_race(data, suf):
    """
        Plots the distribution of perpetrator races for a given dataset.

        This function creates a pie chart to visualize the frequency of different perpetrator races in the provided dataset. It uses a color palette from Seaborn to differentiate the races.

        Parameters:
        - data (DataFrame): The dataset containing homicide information.
        - suf (str): A suffix for the plot title to specify the dataset's context (e.g., 'USA', 'Texas').

        Returns:
        None; the function displays the pie chart directly.
        """
    # Plot the perpetrator race distribution
    colors = sns.color_palette('Spectral')
    perpetrator_race_counts = data['Perpetrator Race'].value_counts()
    labels = perpetrator_race_counts.index
    plt.pie(perpetrator_race_counts, colors=colors)
    # label title and legend
    plt.title(f'Perpetrator Race distribution in {suf}', fontdict={'family': 'sans',
                                                                   'style': 'normal',
                                                                   'color': 'navy',
                                                                   'weight': 'normal',
                                                                   'size': 14})
    plt.legend(loc='center', labels=labels, labelcolor='navy')
    # I want a dont plot instead of a simple pie
    plt.gca().add_artist(plt.Circle((0, 0), 0.7, color='white'))
    # show the plot
    plt.show()

    # ----------------------------------#
    # for the canvas presentation I've also used a code for bar plot:
    # def plot_perpetrator_race_bar(data, suf):
    # Plot the perpetrator race distribution using a bar plot
    # colors = sns.color_palette('Spectral')
    # perpetrator_race_counts = data['Perpetrator Race'].value_counts()
    # labels = perpetrator_race_counts.index

    # Create a bar plot
    # plt.figure(figsize=(10, 6))
    # sns.barplot(x=perpetrator_race_counts.index, y=perpetrator_race_counts, palette=colors)
    # and customizied as above

def plot_population_trend(data1, data2):
    """
        Plots population trends over the years for Texas and California.

        This function compares the population growth of Texas and California from the year 2000 to 2014 using line plots. It uses distinct colors for each state for clear comparison.

        Parameters:
        - data1 (list): Population data for Texas.
        - data2 (list): Population data for California.

        Returns:
        None; the function displays the line plot directly.
    """
    # trend of the population in Texas and California from 2020 to 2014
    plt.plot(range(2000, 2015), data1[20:], color='seagreen', linestyle='-', label='Texas')
    plt.plot(range(2000, 2015), data2[20:], color='olive', linestyle="-", label='California ')
    plt.title('Population Over Years', fontdict={'family': 'sans',
                                                 'style': 'normal',
                                                 'color': 'navy',
                                                 'weight': 'normal',
                                                 'size': 14})
    plt.xlabel('Year', fontdict={'family': 'sans',
                                 'style': 'normal',
                                 'color': 'navy',
                                 'weight': 'normal',
                                 'size': 12})
    plt.ylabel('Population', fontdict={'family': 'sans',
                                       'style': 'normal',
                                       'color': 'navy',
                                       'weight': 'normal',
                                       'size': 12})
    plt.grid(True, linestyle='--', alpha=0.3, color='navy')
    plt.legend()
    # show the plot
    plt.show()

def plot_crimes_countries_trend(data1, data2, suf1, suf2):
    """
        Compares the distribution of crimes over the years in California and Texas.

        This function visualizes the trend of crimes in California and Texas using histograms. It compares the distribution of crimes over the years in these two states, aiming to identify any significant differences or patterns.

        Parameters:
        - data1 (DataFrame): Homicide data for California.
        - data2 (DataFrame): Homicide data for Texas.
        - suf1 (str): Suffix for the plot title indicating California.
        - suf2 (str): Suffix for the plot title indicating Texas.

        Returns:
        None; the function displays the histogram directly.
    """
    i, colors, data, suf = 0, ['olive', 'seagreen'], [data1, data2], [suf1, suf2]
    while i < 2:
        # distribution of crimes through the years: comparison between California and Texas
        sns.histplot(data[i], x='Year', bins=35, multiple='dodge', shrink=.75, color=colors[i], kde=True, label=suf[i])
        i += 1
    # add a title
    plt.title('Crimes count: comparison between California and Texas', fontdict={'family': 'sans',
                                                                                 'style': 'normal',
                                                                                 'color': 'navy',
                                                                                 'weight': 'normal',
                                                                                 'size': 14})
    # Adding grid lines
    plt.grid(True, linestyle='dotted', alpha=0.3, color='navy')
    # add a legend
    plt.legend(labelcolor='navy')
    # show the plot
    plt.show()

def crimes_months(data, suf):
    """
        Displays a bar chart of homicide cases over different months for a given dataset.

        This function creates a bar chart to visualize the count of homicide cases in each month. It aims to identify any monthly trends or patterns in the homicide data.

        Parameters:
        - data (DataFrame): The dataset containing homicide information.
        - suf (str): A suffix for the plot title to specify the dataset's context (e.g., 'USA', 'Texas').

        Returns:
        None; the function displays the bar chart directly.
    """
    import plotly.express as px
    month = data['Month'].value_counts()
    plt.bar(x=month.index,
            height=month, color=sns.color_palette('RdBu', 12))
    plt.xlabel('months')
    plt.xticks(rotation=90)
    plt.title(f'Count Of Homicide Cases Over The Months in {suf}', color='navy')
    for i, value in enumerate(month):
        plt.annotate(str(value), (i, value), ha='center', va='bottom', fontsize=6, color='navy')
    plt.show()

def plot_crimes_capitals_trend(data1, data2, suf1, suf2):
    """
        Compares the distribution of crimes through the years in Sacramento and Austin.

        This function visualizes the trend of crimes in the capital cities of Sacramento and Austin using a histogram. It aims to compare the distribution of crimes over the years in these two cities.

        Parameters:
        - data1 (DataFrame): Homicide data for Sacramento.
        - data2 (DataFrame): Homicide data for Austin.
        - suf1 (str): Suffix for the plot title indicating the first city (Sacramento).
        - suf2 (str): Suffix for the plot title indicating the second city (Austin).

        Returns:
        None; the function displays the histogram directly.
    """
    # distribution of crimes through the years: comparison between Sacramento and Austin
    i, colors = 0, ['olive', 'seagreen']
    for (data, suf) in [(data1, suf1), (data2, suf2)]:
        sns.histplot(data, x='Year', bins=30, multiple='dodge', shrink=.75, color=colors[i], kde=True, label=f'{suf}')
        i += 1
    # add a title
    plt.title('Crimes count: comparison between capitals', fontdict={'family': 'sans',
                                                                     'style': 'normal',
                                                                     'color': 'navy',
                                                                     'weight': 'normal',
                                                                     'size': 14})
    # Adding grid lines
    plt.grid(True, linestyle='dotted', alpha=0.3, color='navy')
    # add a legend
    plt.legend(labelcolor='navy')
    # show the plot
    plt.show()

def plot_solved_crimes(data1, data2, data3, suf1, suf2, suf3):
    """
        Plots the percentage of solved crimes over the years for different datasets.

        This function visualizes how the rate of solved crimes has changed over the years for three different datasets. It uses line plots to show trends in crime solving.

        Parameters:
        - data1, data2, data3 (DataFrame): Datasets containing homicide information.
        - suf1, suf2, suf3 (str): Suffixes for the plot legend to specify each dataset's context.

        Returns:
        None; the function displays the line plot directly.
        """
    # percentage of solved crimes through the years
    i, colors, place = 0, ['seagreen', 'mediumaquamarine', 'cornflowerblue'], [suf1, suf2, suf3]
    for data in [data1, data2, data3]:
        solved_crimes = []
        for j in range(1980, 2015):
            solved_crimes.append(
                len(data[(data['Year'] == j) & (data['Crime Solved'] == 1)]) / len(data[data['Year'] == j]))
        plt.plot(range(1980, 2015), solved_crimes, color=colors[i], label=f'{place[i]}')
        i += 1
    # Adding grid lines
    plt.grid(True, linestyle='-', alpha=0.3, color='navy')
    # add a legend
    plt.legend(labelcolor='navy')
    # add title
    plt.title(f'Percentage of solved crimes', fontdict={'family': 'sans',
                                                        'style': 'normal',
                                                        'color': 'navy',
                                                        'weight': 'normal',
                                                        'size': 14})
    # show the plot
    plt.show()

def plot_used_deadly_weapons_matplotlib(data, suf, weapon_color_mapping):
    # Prepare data
    weapon_counts = data['Weapon'].value_counts().head(10)
    labels = weapon_counts.index
    counts = weapon_counts.values
    total_count = counts.sum()
    percentages = [f'{(count / total_count * 100):.1f}%' for count in counts]

    # Assign colors to each label from the color mapping
    pie_colors = [weapon_color_mapping[weapon] for weapon in labels]

    # Set seaborn style
    sns.set(style="whitegrid")

    # Create pie chart
    fig, ax = plt.subplots()
    wedges, _, autotexts = ax.pie(counts, labels=None, autopct='', startangle=140, colors=pie_colors)

    # Calculate label positions and determine if arrow is needed
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        x = np.cos(np.deg2rad(ang))
        y = np.sin(np.deg2rad(ang))

        # Determine if label should be inside or outside the slice
        inside_slice = (p.theta2 - p.theta1) >= 10  # Threshold angle for inside
        if inside_slice:
            # Set the inside label
            plt.setp(autotexts[i], text=percentages[i], size=10, weight='normal', color='black')
        else:
            # Annotate outside label
            xytext = (1.3 * x, 1.3 * y)  # Adjust this for arrow length
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            ax.annotate(percentages[i], xy=(x, y), xytext=xytext,
                        textcoords='data', ha='left' if x > 0 else 'right', va='center',
                        fontsize=10, color='black',
                        arrowprops=dict(arrowstyle='-', color='black'))

    # Create a legend
    ax.legend(wedges, labels, title="Weapons", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Set title
    ax.set_title(f'Most Used Weapons Overall in {suf}')

    # Save plot as a PNG file with a transparent background
    plt.savefig(f'used_deadly_weapons_{suf}.png', transparent=True, bbox_inches='tight')

    plt.show()

def plot_most_deadly_weapons_matplotlib(data, suf, weapon_color_mapping):
    # Prepare data
    weapon_victim_counts = data.groupby('Weapon')['Victim Count'].sum().nlargest(10)
    labels = weapon_victim_counts.index
    counts = weapon_victim_counts.values
    total_count = counts.sum()
    percentages = [f'{(count / total_count * 100):.1f}%' for count in counts]

    # Assign colors to each label from the color mapping
    pie_colors = [weapon_color_mapping[weapon] for weapon in labels]

    # Set seaborn style
    sns.set(style="whitegrid")

    # Create pie chart
    fig, ax = plt.subplots()
    wedges, _, autotexts = ax.pie(counts, labels=None, autopct='', startangle=140, colors=pie_colors)

    # Calculate label positions and determine if arrow is needed
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        x = np.cos(np.deg2rad(ang))
        y = np.sin(np.deg2rad(ang))

        # Determine if label should be inside or outside the slice
        inside_slice = (p.theta2 - p.theta1) >= 10  # Threshold angle for inside
        if inside_slice:
            # Set the inside label
            plt.setp(autotexts[i], text=percentages[i], size=10, weight='normal', color='black')
        else:
            # Annotate outside label
            xytext = (1.3 * x, 1.3 * y)  # Adjust this for arrow length
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            ax.annotate(percentages[i], xy=(x, y), xytext=xytext,
                        textcoords='data', ha='left' if x > 0 else 'right', va='center',
                        fontsize=10, color='black',
                        arrowprops=dict(arrowstyle='-', color='black'))

    # Create a legend
    ax.legend(wedges, labels, title="Weapons", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Set title
    ax.set_title(f'Deadliest Weapons in {suf}')

    # Save plot as a PNG file with a transparent background
    plt.savefig(f'deadly_weapons_victim_count_{suf}.png', transparent=True, bbox_inches='tight')

    plt.show()

def plot_preferred_weapon_by_race_altair(data, suf, weapon_color_mapping):
    weapon_by_race = data.groupby(['Perpetrator Race', 'Weapon']).size().reset_index(name='Count')
    top_races = weapon_by_race.groupby('Perpetrator Race')['Count'].sum().nlargest(5).reset_index()['Perpetrator Race']
    filtered_weapon_by_race = weapon_by_race[weapon_by_race['Perpetrator Race'].isin(top_races)]

    # Interactive selections for filtering
    selection_race = alt.selection_point(fields=['Perpetrator Race'], bind='legend')
    selection_weapon = alt.selection_point(fields=['Weapon'], bind='legend')

    # Enhanced tooltips
    tooltips = [
        alt.Tooltip('Perpetrator Race', title='Race'),
        alt.Tooltip('Weapon', title='Weapon'),
        alt.Tooltip('Count', title='Count'),
        # Additional tooltip info can be added here
    ]

    # Creating the chart
    chart = alt.Chart(filtered_weapon_by_race).mark_bar().encode(
        x='Perpetrator Race',
        y='Count',
        color=alt.Color('Weapon', scale=alt.Scale(domain=list(weapon_color_mapping.keys()),
                                                  range=list(weapon_color_mapping.values()))),
        tooltip=tooltips
    ).add_params(
        selection_race
    ).add_params(
        selection_weapon
    ).transform_filter(
        selection_race
    ).transform_filter(
        selection_weapon
    ).properties(
        title={
            "text": f'Preferred Weapon by Race in {suf}',
            "subtitle": "Click legend to filter"
        },
        width=700,
        height=500
    ).configure_title(
        font='sans',
        fontSize=16,
        color='navy'
    ).configure_axis(
        labelFont='sans',
        labelFontSize=14,
        labelColor='navy',
        titleFont='sans',
        titleFontSize=14,
        titleColor='navy'
    ).interactive()

    return chart

def plot_statewise_homicide_distribution(homicide_df):
    """
    Generates a bar chart visualizing the distribution of homicides across different states in the USA.

    This function reads a CSV file containing homicide data, aggregates the number of homicides per state, and then uses Altair to create a bar chart. Each state is represented by a bar, with unique colors assigned to each state. The chart is saved as an HTML file.

    Parameters:
    - homicide_data_path (str): The file path to the CSV file containing homicide data. The file should include a 'State' column.

    Returns:
    None; the function creates and saves a bar chart as an HTML file named 'statewise_distribution.html'.

    Example usage:
    plot_statewise_homicide_distribution('path_to_homicide_data.csv')
    """
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

    # Save the chart as an HTML file
    statewise_chart.save('statewise_distribution.html')

def plot_statewise_homicide_heatmap(homicide_df):
    """
    Generates a choropleth map visualizing the distribution of homicides across different states in the USA.

    This function reads a CSV file containing homicide data, converts full state names to their two-letter abbreviations, aggregates the number of homicides per state, and then creates a choropleth map using Plotly. The map highlights the intensity of homicides in each state with a color gradient.

    Parameters:
    - homicide_data_path (str): The file path to the CSV file containing homicide data. The file should include a 'State' column with full state names.

    Returns:
    None; the function creates and displays an interactive choropleth map.

    Example usage:
    plot_statewise_homicide_heatmap('path_to_homicide_data.csv')
    """
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

    # Convert full state names to abbreviations in the dataset
    homicide_df['State'] = homicide_df['State'].map(state_abbreviations)

    # Aggregate data by state
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

    # Set the background to transparent
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)'  # Transparent plot background
    )

    # Show the plot
    fig.show()

def plot_homicide_distribution(homicide_df, city_coords_path):
    """
        Generates a scatter plot on a geographical map showing the distribution of homicides in various cities across the USA.

        This function takes two CSV files: one containing homicide data and the other containing city coordinates. It merges these datasets based on city names, aggregates the number of homicides per city, and then creates a scatter plot using Plotly to visualize this data on a map of the USA. The plot includes customization options for the appearance and displays cities with the size of markers proportional to the number of homicides.

        Parameters:
        - homicide_data_path (str): The file path to the CSV file containing homicide data. This file should include at least the columns for city names.
        - city_coords_path (str): The file path to the CSV file containing city coordinates. This file should include city names, latitude, and longitude.

        Returns:
        None; the function creates and displays an interactive scatter plot using Plotly.

        Example usage:
        plot_homicide_distribution('path_to_homicide_data.csv', 'path_to_city_coords.csv')
        """
    # Load the city coordinates dataset
    city_coords_df = pd.read_csv(city_coords_path, low_memory=False)

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
        font=dict(family='sans', size=14, color='navy'),
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)'
    )

    # Show the plot
    fig.show()

def main():
    """
    Main function to perform an extensive analysis on homicide data.

    The function carries out the following tasks:
    1. Imports the homicide dataset and converts it to a DataFrame.
    2. Provides an overview of the dataset, including descriptive statistics, information on columns, and checks for missing values.
    3. Reduces the dataset to focus on relevant columns for further analysis.
    4. Extracts specific subsets of data for detailed comparison, focusing on Texas, California, Austin, and Sacramento.
    5. Conducts data cleaning and transformation, including handling outliers and converting categorical variables.
    6. Analyzes population data for the United States, Texas, and California, plotting population trends.
    7. Performs a variety of analyses at both the national and state levels, including racial demographics of victims and perpetrators, age trends, and crime solutions.
    8. Compares crime rates in capital cities to overall state rates.
    9. Creates visualizations of crime trends and preferred weapons by race, using custom color palettes for weapons.
    10. Saves generated visualizations as HTML files and performs city-wise, state-wise, and heatmap plotting of homicide data.

    No parameters are required, and no return value is produced.
    The function relies on other plotting functions and data processing steps, culminating in a comprehensive exploration of the homicide dataset.
    """
    # import the dataset
    homicide = pd.read_csv("database.csv", low_memory=False)
    # convert the dataset to dataframe class
    homicide_df = pd.DataFrame(homicide)

    # overview
    print(homicide_df.describe().T)
    homicide_df.info
    print(homicide_df.columns)
    # check for na values in the dataframe
    print(homicide_df.isnull().values.any())
    col_info = [(col, dtype) for col, dtype in zip(homicide_df.columns, homicide_df.dtypes)]
    print(tbl.tabulate(col_info, headers=['Variable', 'Class'], tablefmt='pretty'))

    # maintain some columns only: we're not interested to keep them all for our purposes
    homicide_df = homicide_df[
        ['City', 'State', 'Year', 'Month', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age', 'Victim Race',
         'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Weapon', 'Relationship','Victim Count']]

    # specific datasets we extract to get insights via comparisons
    homicide_Texas = homicide_df[homicide_df['State'] == 'Texas']
    homicide_California = homicide_df[homicide_df['State'] == 'California']
    homicide_Austin = homicide_df[homicide_df['City'] == 'Austin']
    homicide_Sacramento = homicide_df[homicide_df['City'] == 'Sacramento']

    # still: data cleaning
    # we have two numerical variables. We want to convert the other ones properly, if we need so for EDA.

    # crime type
    set(homicide_df['Crime Type'])
    # {'Manslaughter by Negligence', 'Murder or Manslaughter'}
    homicide_df['Crime Type'] = homicide_df['Crime Type'].replace(
        {'Murder or Manslaughter': 1, 'Manslaughter by Negligence': 0})
    # we rename the column to get at a glance the interpretation of the numerical values we now have throughout the rows
    homicide_df = homicide_df.rename(columns={'Crime Type': 'Crime Type: intentional manslaughter?'})

    # crime solved
    set(homicide_df['Crime Solved'])
    # {'Yes','No'}
    homicide_df['Crime Solved'] = homicide_df['Crime Solved'].replace({'Yes': 1, 'No': 0})
    homicide_California['Crime Solved'] = homicide_California['Crime Solved'].replace({'Yes': 1, 'No': 0})
    homicide_Texas['Crime Solved'] = homicide_Texas['Crime Solved'].replace({'Yes': 1, 'No': 0})

    # victim sex: we want to keep it as categorical for the EDA
    set(homicide_df['Victim Sex'])

    # perpetrator sex: we want to keep it as categorical for the EDA
    set(homicide_California['Perpetrator Sex'])

    # victim age: outliers findings
    set(homicide_df['Victim Age'])
    # here we have outliers: (age 998) !! We then decided to delete that row
    homicide_df = homicide_df[homicide_df['Victim Age'] != 998]

    # perpetrator age
    set(homicide_California['Perpetrator Age'])
    # outliers 95/05 : per Edo
    homicide_df = homicide_df[homicide_df['Perpetrator Age'] != 0]

    # perpetrator race
    set(homicide_California['Perpetrator Race'])
    # {'Asian/Pacific Islander', 'White', 'Black', 'Native American/Alaska Native', 'Unknown'}

    # perpetrator ethnicity
    set(homicide_California['Perpetrator Ethnicity'])
    # {'Asian/Pacific Islander', 'White', 'Black', 'Native American/Alaska Native', 'Unknown'}

    # population in Texas and California: extention of the research
    population = pd.read_csv('population_usafacts.csv')

    # population US
    pop = []
    for i in range(1980, 2015):
        pop.append(population[f'{i}'][0])

    # population California
    pop_cal = []
    for i in range(81, 116):
        pop_cal.append(population.iloc[25, i])

    # population Texas:
    pop_tex = []
    for i in range(81, 116):
        pop_tex.append(population.iloc[64, i])

    plot_population_trend(pop_tex, pop_cal)
    print(homicide_df['Victim Race'].value_counts())
    print(homicide_df['Perpetrator Race'].value_counts())
    print(homicide_California['Victim Race'].value_counts())
    print(homicide_California['Perpetrator Race'].value_counts())
    print(homicide_Texas['Victim Race'].value_counts())
    print(homicide_Texas['Perpetrator Race'].value_counts())
    print(homicide_df[homicide_df['Victim Race'] == 'Unknown'].shape[0] / homicide_df.shape[0])
    print(homicide_df[homicide_df['Perpetrator Race'] == 'Unknown'].shape[0] / homicide_df.shape[0])

    plot_victim_race(homicide_df, 'Total')
    plot_perpetrator_race(homicide_df, 'Total')
    plot_perpetrator_race(homicide_df[homicide_df['Perpetrator Race'] != 'Unknown'], 'Total without Unknown')

    for state in ['California', 'Texas']:
        plot_perpetrator_race(homicide_df[homicide_df['State'] == state], state)
    for state in ['California', 'Texas']:
        plot_perpetrator_race(
            homicide_df[(homicide_df['State'] == state) & (homicide_df['Perpetrator Race'] != 'Unknown')],
            f'{state} but without unknown')

    # to write a different code, let's plot the victim race pie for all the states
    for state in ['California', 'Texas']:
        plot_victim_race(homicide_df[homicide_df['State'] == state], state)

    plot_victim_age_trend(homicide_df, homicide_California, homicide_Texas, 'US', 'California', 'Texas')

    plot_perpetrator_age_trend(homicide_df, homicide_California, homicide_Texas, 'US', 'California', 'Texas')

    # % of homocides in capitals
    print(
        f'Be aware the proportion of homicides in the capital city in respect to the entire country is very different bewteen California and Texas.',
        f"The % is indeed {len(homicide_Sacramento) / len(homicide_California)} for California, while it's {len(homicide_Austin) / len(homicide_Texas)} for Texas")
    plot_crimes_countries_trend(homicide_California, homicide_Texas, 'California', 'Texas')
    plot_crimes_capitals_trend(homicide_Sacramento, homicide_Austin, 'Sacramento', 'Austin')

    plot_solved_crimes(homicide_df, homicide_California, homicide_Texas, 'US', 'California', 'Texas')
    for (data, suf) in [(homicide_df, 'US'), (homicide_California, 'California'), (homicide_Texas, 'Texas')]:
        crimes_months(data, suf)
    # Define a color palette for visualizing different weapons
    weapon_palette =  [
    '#FFD700',  # Gold
    '#FFC0CB',  # Light Pink
    '#98FB98',  # Pale Green
    '#87CEFA',  # Light Sky Blue
    '#BA55D3',  # Medium Orchid
    '#FFA07A',  # Light Salmon
    '#20B2AA',  # Light Sea Green
    '#778899',  # Light Slate Gray
    '#FFDEAD',  # Navajo White
    '#F0E68C',  # Khaki
]

    # Map each weapon to a color from the palette
    weapon_counts = homicide_df['Weapon'].value_counts()
    weapon_color_mapping = {weapon: weapon_palette[i % len(weapon_palette)] for i, weapon in
                            enumerate(weapon_counts.index)}

    # National level analysis: plots and visualizations
    chart_national = plot_preferred_weapon_by_race_altair(homicide_df, 'USA', weapon_color_mapping)
    plot_used_deadly_weapons_matplotlib(homicide_df, 'USA', weapon_color_mapping)
    plot_most_deadly_weapons_matplotlib(homicide_df, 'USA', weapon_color_mapping)

    # State-specific analysis for Texas
    homicide_Texas = homicide_df[homicide_df['State'] == 'Texas']
    chart_texas = plot_preferred_weapon_by_race_altair(homicide_Texas, 'Texas', weapon_color_mapping)
    plot_used_deadly_weapons_matplotlib(homicide_Texas, 'Texas', weapon_color_mapping)
    plot_most_deadly_weapons_matplotlib(homicide_Texas, 'Texas', weapon_color_mapping)

    # State-specific analysis for California
    homicide_California = homicide_df[homicide_df['State'] == 'California']
    chart_california = plot_preferred_weapon_by_race_altair(homicide_California, 'California', weapon_color_mapping)
    plot_used_deadly_weapons_matplotlib(homicide_California, 'California', weapon_color_mapping)
    plot_most_deadly_weapons_matplotlib(homicide_California, 'California', weapon_color_mapping)

    # Save the charts as HTML files
    chart_national.save('chart_national.html')
    chart_texas.save('chart_texas.html')
    chart_california.save('chart_california.html')

    #city-wise plotting
    plot_homicide_distribution(homicide_df, 'us_cities.csv')
    #state-wise plotting
    plot_statewise_homicide_distribution(homicide_df)
    #heat-map plotting
    plot_statewise_homicide_heatmap(homicide_df)

if __name__ == "__main__":
    main()

