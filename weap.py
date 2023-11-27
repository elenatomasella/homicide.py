import altair as alt
import pandas as pd

def plot_used_deadly_weapons_altair(data, suf, weapon_color_mapping):
    weapon_counts = data['Weapon'].value_counts().reset_index()
    weapon_counts.columns = ['Weapon', 'Count']

    chart = alt.Chart(weapon_counts.head(10)).mark_bar(cornerRadius=3).encode(
        x=alt.X('Weapon', sort='-y', title='Weapon', axis=alt.Axis(grid=False)),
        y=alt.Y('Count', title='Count', axis=alt.Axis(grid=True)),
        color=alt.Color('Weapon', scale=alt.Scale(domain=list(weapon_color_mapping.keys()),
                                                  range=list(weapon_color_mapping.values())))
    ).properties(
        title=f'Most Used Weapons Overall in {suf}',
        width=600,
        height=400
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
        gridColor = 'lightgray'
    )

    return chart

def plot_most_deadly_weapons_altair(data, suf, weapon_color_mapping):
    weapon_victim_counts = data.groupby('Weapon')['Victim Count'].sum().reset_index()
    weapon_victim_counts.columns = ['Weapon', 'Total Victim Count']

    chart = alt.Chart(weapon_victim_counts).mark_bar(cornerRadius=3).encode(
        x=alt.X('Weapon', sort='-y', title='Weapon', axis=alt.Axis(grid=False)),
        y=alt.Y('Total Victim Count', title='Total Victim Count', axis=alt.Axis(grid=True)),
        color=alt.Color('Weapon', scale=alt.Scale(domain=list(weapon_color_mapping.keys()), range=list(weapon_color_mapping.values())))
    ).properties(
        title=f'Deadliest Weapons Based on Victim Count in {suf}',
        width=600,
        height=400
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

    return chart


def plot_preferred_weapon_by_race_altair(data, suf, weapon_color_mapping):
    weapon_by_race = data.groupby(['Perpetrator Race', 'Weapon']).size().reset_index(name='Count')
    top_races = weapon_by_race.groupby('Perpetrator Race')['Count'].sum().nlargest(5).reset_index()['Perpetrator Race']
    filtered_weapon_by_race = weapon_by_race[weapon_by_race['Perpetrator Race'].isin(top_races)]

    chart = alt.Chart(filtered_weapon_by_race).mark_bar().encode(
        x='Perpetrator Race',
        y='Count',
        color=alt.Color('Weapon', scale=alt.Scale(domain=list(weapon_color_mapping.keys()), range=list(weapon_color_mapping.values()))),
        tooltip=['Weapon', 'Count']
    ).properties(
        title=f'Preferred Weapon by Race in {suf}',
        width=700,
        height=500
    ).configure_title(
        font='sans',
        fontSize=14,
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



# [Include the Altair plotting functions here: plot_used_deadly_weapons_altair, plot_most_deadly_weapons_altair, plot_preferred_weapon_by_race_altair]

def main():
    # Import the dataset
    homicide = pd.read_csv("database.csv", low_memory=False)
    homicide_df = pd.DataFrame(homicide)

    # Reduction of the dataset
    homicide_df = homicide_df[
        ['City', 'State', 'Year', 'Month', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age', 'Victim Race',
         'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Weapon', 'Relationship', 'Victim Count']]
    # Define a color palette that tends towards pink, with enough colors for each weapon
    weapon_palette = [
    '#264653',  # Dark Cyan
    '#2A9D8F',  # Teal
    '#E9C46A',  # Sandy Brown
    '#F4A261',  # Light Orange
    '#E76F51',  # Burnt Sienna
    '#D62828',  # Dark Red
    '#023E8A',  # Royal Blue
    '#0077B6',  # Ocean Blue
    '#0096C7',  # Sky Blue
    '#48CAE4',  # Light Blue
    # Additional colors can be added if more categories are needed
    ]

    # Map each weapon to a color from the palette
    weapon_counts = homicide_df['Weapon'].value_counts()
    weapon_color_mapping = {weapon: weapon_palette[i % len(weapon_palette)] for i, weapon in
                            enumerate(weapon_counts.index)}

    # National level analysis
    chart_national1 = plot_used_deadly_weapons_altair(homicide_df, 'USA', weapon_color_mapping)
    chart_national2 = plot_most_deadly_weapons_altair(homicide_df, 'USA', weapon_color_mapping)
    chart_national3 = plot_preferred_weapon_by_race_altair(homicide_df, 'USA', weapon_color_mapping)

    # State-specific analysis for Texas
    homicide_Texas = homicide_df[homicide_df['State'] == 'Texas']
    chart_texas1 = plot_used_deadly_weapons_altair(homicide_Texas, 'Texas', weapon_color_mapping)
    chart_texas2 = plot_most_deadly_weapons_altair(homicide_Texas, 'Texas', weapon_color_mapping)
    chart_texas3 = plot_preferred_weapon_by_race_altair(homicide_Texas, 'Texas', weapon_color_mapping)

    # State-specific analysis for California
    homicide_California = homicide_df[homicide_df['State'] == 'California']
    chart_california1 = plot_used_deadly_weapons_altair(homicide_California, 'California', weapon_color_mapping)
    chart_california2 = plot_most_deadly_weapons_altair(homicide_California, 'California', weapon_color_mapping)
    chart_california3 = plot_preferred_weapon_by_race_altair(homicide_California, 'California', weapon_color_mapping)

    # Replace display() with save() for charts
    chart_national1.save('chart_national1.html')
    chart_national2.save('chart_national2.html')
    chart_national3.save('chart_national3.html')

    chart_texas1.save('chart_texas1.html')
    chart_texas2.save('chart_texas2.html')
    chart_texas3.save('chart_texas3.html')

    chart_california1.save('chart_california1.html')
    chart_california2.save('chart_california2.html')
    chart_california3.save('chart_california3.html')

if __name__ == "__main__":
    main()
