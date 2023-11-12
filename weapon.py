import matplotlib
print(matplotlib.get_backend())
matplotlib.use('TkAgg')  # Or another backend suitable for your environment
import pandas as pd
import matplotlib.pyplot as plt

def plot_used_deadly_weapons(data, suf):
    """Plot the most deadly weapons overall."""
    weapon_counts = data['Weapon'].value_counts()
    plt.figure(figsize=(10, 6))
    weapon_counts.head(10).plot(kind='bar', color='skyblue')
    plt.title(f'Most Used Weapons Overall in {suf}')  # Corrected to use f-string
    plt.xlabel('Weapon')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()


def plot_most_deadly_weapons(data, suf):
    """Plot the deadliest weapons based on the total number of victims."""
    weapon_victim_counts = data.groupby('Weapon')['Victim Count'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    weapon_victim_counts.head(10).plot(kind='bar', color='skyblue')
    plt.title(f'Deadliest Weapons Based on Victim Count in {suf}')
    plt.xlabel('Weapon')
    plt.ylabel('Total Victim Count')
    plt.xticks(rotation=45)
    plt.show()


def plot_preferred_weapon_by_race(data, suf):
    """Plot the preferred weapon by race."""
    weapon_by_race = data.groupby('Perpetrator Race')['Weapon'].value_counts().unstack(fill_value=0)
    top_races = weapon_by_race.sum(axis=1).sort_values(ascending=False).head(5).index
    top_weapons = weapon_by_race.sum().sort_values(ascending=False).head(10).index
    filtered_weapon_by_race = weapon_by_race.loc[top_races, top_weapons]

    plt.figure(figsize=(12, 8))
    filtered_weapon_by_race.plot(kind='bar', stacked=True, colormap='viridis')
    plt.title(f'Preferred Weapon by Race in {suf}')  # Corrected to use f-string
    plt.xlabel('Race')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Weapon', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()




def main():
    # import the dataset
    homicide = pd.read_csv("database.csv", low_memory=False)
    homicide_df = pd.DataFrame(homicide)
    # reduction of the dataset
    print(homicide_df.columns)
    homicide_df = homicide_df[
        ['City', 'State', 'Year', 'Month', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age', 'Victim Race',
         'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Weapon', 'Relationship', 'Victim Count']]
    homicide_df = homicide_df[homicide_df['State'].isin(['Texas', 'California'])]
    # specific datasets we extract to get insights via comparisons
    homicide_Texas = homicide_df[homicide_df['State'] == 'Texas']
    homicide_California = homicide_df[homicide_df['State'] == 'California']
    #homicide_Austin = homicide_df[homicide_df['City'] == 'Austin']
    #homicide_Sacramento = homicide_df[homicide_df['City'] == 'Sacramento']

    plot_used_deadly_weapons(homicide_df, 'Total')
    plot_most_deadly_weapons(homicide_df, 'Total')
    plot_preferred_weapon_by_race(homicide_df, 'Total')
    plot_used_deadly_weapons(homicide_df, 'Texas')
    plot_most_deadly_weapons(homicide_Texas, 'Texas')
    plot_preferred_weapon_by_race(homicide_Texas, 'Texas')
    plot_used_deadly_weapons(homicide_df, 'California')
    plot_most_deadly_weapons(homicide_California, 'California')
    plot_preferred_weapon_by_race(homicide_California, 'California')




if __name__ == "__main__":
    main()
