#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_victim_age_trend(data, suf):
    """" Group the data by 'Year' and calculate median """
    data['Victim Age'] = pd.to_numeric(data['Victim Age'], errors='coerce')
    grouped_data = data.groupby('Year')['Victim Age'].agg(['median']).reset_index()
    #.agg is used to use functions on each group identify by groupby
    plt.plot(grouped_data['Year'], grouped_data['median'], label='Median Age')
    plt.xlabel('Year')
    plt.ylabel('Age')
    plt.title(f'Median Victim Age Through the Years in {suf}')
    plt.legend()
    plt.show()

def plot_perpetrator_age_trend(data, suf):
    data['Perpetrator Age'] = pd.to_numeric(data['Perpetrator Age'], errors='coerce')
    """" Group the data by 'Year' and calculate median """
    grouped_data = data.groupby('Year')['Perpetrator Age'].agg(['median']).reset_index()
    #.agg is used to use functions on each group identify by groupby
    plt.plot(grouped_data['Year'], grouped_data['median'], label='Median Age')
    plt.xlabel('Year')
    plt.ylabel('Age')
    plt.title(f'Median Perpetrator Age Through the Years in {suf}')
    plt.legend()
    plt.show()

#EDA about victim race
def plot_victim_race_distribution(data, suf):
    # Plot the victim race distribution
    labels = set(data['Victim Race'])
    colors = ['dimgrey', 'brown', 'snow', 'burlywood', 'turquoise']
    victim_race_counts = data['Victim Race'].value_counts()
    plt.pie(victim_race_counts, colors=colors, shadow=True, startangle=140)
    plt.title(f'Victim Race distribution in {suf}')
    plt.legend(title='Races', loc='lower center', labels=labels)
    plt.show()

#EDA about perpetrator race
def plot_perpetrator_race(data, suf):
    # Plot the perpetrator race distribution
    labels = set(data['Perpetrator Race'])
    colors = ['dimgrey', 'brown', 'snow', 'burlywood', 'turquoise']
    perpetrator_race_counts = data['Perpetrator Race'].value_counts()
    plt.pie(perpetrator_race_counts, colors=colors)
    plt.title(f'Perpetrator Race distribution in {suf}')
    plt.legend(title='Races', loc='upper center', labels=labels)
    plt.show()

def plot_crimes_countries_trend(data):
    # distribution of crimes through the years: comparison between California and Texas
    sns.histplot(data, x='Year', hue='State', bins=35, multiple='dodge', shrink=.75, palette=['orchid', 'navy'])
    plt.title('Crimes count: comparison between California and Texas')
    plt.legend()
    plt.show()

def plot_crimes_capitals_trend(data):
    # distribution of crimes through the years: comparison between Sacramento and Austin
    sns.histplot(data[(data['City'] == 'Austin') | (data['City'] == 'Sacramento')], x='Year',
                 hue='City', bins=30, multiple='dodge', shrink=.75, palette=['orchid', 'navy'])
    plt.title('Crimes count: comparison between capitals')
    plt.show()

def plot_solved_crimes(data, suf):
    #percentage of solved crimes through the years
    solved_crimes = []
    for i in list(set(data['Year'])):
        solved_crimes.append(len(data[(data['Year'] == i) & (data['Crime Solved'] == 1)]) / len(data[data['Year'] == i]))
    plt.plot(range(1980, 2015), solved_crimes, color='peachpuff', label='generic')
    plt.legend()
    plt.title(f'Percentage of solved crimes in {suf}')
    plt.show()

def plot_population_trend(data1,data2):
    # trend of the population in Texas and California from 2020 to 2014
    plt.plot(range(2000, 2015), data1[20:], color='navy', linestyle='--', label='Texas')
    plt.plot(range(2000, 2015), data2[20:], color='orchid', linestyle="--", label='California ')
    plt.title('Population Over Years')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.show()



def main():
    # import the dataset
    homicide = pd.read_csv("database.csv", low_memory=False)
    #convert the dataset to dataframe class
    homicide_df = pd.DataFrame(homicide)

    #overview
    print(homicide_df.describe().T)
    homicide_df.info
    print(homicide_df.columns)
    # check for na values in the dataframe
    print(homicide_df.isnull().values.any())

    #maintain some columns only: we're not interested to keep them all for our purposes
    homicide_df = homicide_df[['City', 'State', 'Year', 'Month', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age', 'Victim Race',
         'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Weapon', 'Relationship']]

    #we want to investigate the subset of observations concerning California and Texas so we will keep those rows only
    homicide_df = homicide_df[homicide_df['State'].isin(['Texas', 'California'])]
    # specific datasets we extract to get insights via comparisons
    homicide_Texas = homicide_df[homicide_df['State'] == 'Texas']
    homicide_California = homicide_df[homicide_df['State'] == 'California']
    homicide_Austin = homicide_df[homicide_df['City'] == 'Austin']
    homicide_Sacramento = homicide_df[homicide_df['City'] == 'Sacramento']

    #still: data cleaning
    # we have two numerical variables. We want to convert the other ones properly, if we need so for EDA.

    #crime type
    set(homicide_df['Crime Type'])
    # {'Manslaughter by Negligence', 'Murder or Manslaughter'}
    homicide_df['Crime Type'] = homicide_df['Crime Type'].replace({'Murder or Manslaughter': 1, 'Manslaughter by Negligence': 0})
    #we rename the column to get at a glance the interpretation of the numerical values we now have throughout the rows
    homicide_df = homicide_df.rename(columns={'Crime Type': 'Crime Type: intentional manslaughter?'})

    #crime solved
    set(homicide_df['Crime Solved'])
    #{'Yes','No'}
    homicide_df['Crime Solved'] = homicide_df['Crime Solved'].replace({'Yes': 1, 'No': 0})
    homicide_California['Crime Solved'] = homicide_California['Crime Solved'].replace({'Yes': 1, 'No': 0})
    homicide_Texas['Crime Solved'] = homicide_Texas['Crime Solved'].replace({'Yes': 1, 'No': 0})

    #victim sex: we want to keep it as categorical for the EDA
    set(homicide_df['Victim Sex'])

    #perpetrator sex: we want to keep it as categorical for the EDA
    set(homicide_California['Perpetrator Sex'])

    #victim age: outliers findings
    set(homicide_df['Victim Age'])
    # here we have outliers: (age 998) !! We then decided to delete that row
    homicide_df = homicide_df[homicide_df['Victim Age'] != 998]

    #perpetrator age
    set(homicide_California['Perpetrator Age'])
    # outliers 95/05 : per Edo
    homicide_df = homicide_df[homicide_df['Perpetrator Age'] != 0]

    #perpetrator race
    set(homicide_California['Perpetrator Race'])
    # {'Asian/Pacific Islander', 'White', 'Black', 'Native American/Alaska Native', 'Unknown'}

    #perpetrator ethnicity
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

    plot_victim_age_trend(homicide_df, 'Total')
    plot_victim_age_trend(homicide_California, 'California')
    plot_victim_age_trend(homicide_Texas, 'Texas')

    plot_perpetrator_age_trend(homicide_df,'Total')
    plot_perpetrator_age_trend(homicide_California, 'California')
    plot_perpetrator_age_trend(homicide_Texas,'Texas')

    plot_victim_race_distribution(homicide_df, 'Total')
    plot_victim_race_distribution(homicide_California, 'California')
    plot_victim_race_distribution(homicide_Texas, 'Texas')

    plot_perpetrator_race(homicide_df, 'Total')
    plot_perpetrator_race(homicide_California, 'California')
    plot_perpetrator_race(homicide_Texas, 'Texas')

    # % of homocides in capitals
    print(f'Be aware the proportion oh homicides in the capital city in respect to the entire country is very different bewteen California and Texas.',
          "The % is indeed {len(homicide_Sacramento) / len(homicide_California)} for California, while it's {len(homicide_Austin) / len(homicide_Texas)} for Texas")
    plot_population_trend(pop_tex,pop_cal)
    plot_crimes_countries_trend(homicide_df)
    plot_crimes_capitals_trend(homicide_df)

    plot_solved_crimes(homicide_df, 'Total')
    plot_solved_crimes(homicide_California, 'California')
    plot_solved_crimes(homicide_Texas, 'Texas')


if __name__ == "__main__":
    main()
