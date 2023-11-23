#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_victim_age_trend(data1, data2, data3, suf1,suf2,suf3):
    """" Group the data by 'Year' and calculate mean """
    i, colors = 0, ['orchid', 'mediumaquamarine','cornflowerblue']
    for (data,suf) in [(data1,suf1),(data2,suf2),(data3,suf3)]:
        # Convert 'Victim Age' to numeric
        data['Victim Age'] = pd.to_numeric(data['Victim Age'], errors='coerce')
        # Group data by 'Year' and calculate median
        grouped_data = data.groupby('Year')['Victim Age'].agg(['mean']).reset_index()
        #.agg is used to use functions on each group identify by groupby
        plt.plot(grouped_data['Year'], grouped_data['mean'],  marker='o', linestyle='-', color=colors[i],label=f'Average Age in {suf}')
        i+=1
    #adding labels and title
    plt.xlabel('year', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':12})
    plt.ylabel('age',fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':12})
    plt.title(f'Victim Age Through the Years',fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
    
    # Adding grid lines
    plt.grid(True, linestyle='--', alpha=0.7, color = 'navy')
    #add a legend
    plt.legend(labelcolor = 'navy')
    #show the plot
    plt.show()

def plot_perpetrator_age_trend(data1,data2,data3, suf1,suf2,suf3):
    i, colors = 0, ['orchid', 'mediumaquamarine','cornflowerblue']
    for (data,suf) in [(data1,suf1),(data2,suf2),(data3,suf3)]:
        data['Perpetrator Age'] = pd.to_numeric(data['Perpetrator Age'], errors='coerce')
        """" Group the data by 'Year' and calculate mean """
        grouped_data = data.groupby('Year')['Perpetrator Age'].agg(['mean']).reset_index()
        #.agg is used to use functions on each group identify by groupby
        plt.plot(grouped_data['Year'], grouped_data['mean'], marker='o', linestyle='-', color=colors[i],label=f'Average Age in {suf}')
        i+=1
    #adding labels and title
    plt.xlabel('year', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':12})
    plt.ylabel('age',fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':12})
    plt.title(f'Perpetrator Age Through the Years in {suf}',fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
    # Adding grid lines
    plt.grid(True, linestyle='--', alpha=0.7, color = 'navy')
    #add a legend
    plt.legend(labelcolor = 'navy')
    #show the plot
    plt.show()

#EDA about victim race
def plot_victim_race(data, suf):
    # Plot the victim race distribution
    labels = list(set(data['Victim Race']))
    colors = sns.color_palette('PiYG')
    victim_race_counts = data['Victim Race'].value_counts()
    plt.pie(victim_race_counts, colors=colors, startangle=140)
    #label title and legend
    plt.title(f'Victim Race distribution in {suf}', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
    plt.legend(loc='center', labels=labels, labelcolor= 'navy')
    #I want a dont plot instead of a simple pie
    plt.gca().add_artist(plt.Circle((0,0),0.7, color='white'))
    #show the plot
    plt.show()

#EDA about perpetrator race
def plot_perpetrator_race(data, suf):
    # Plot the perpetrator race distribution
    labels = list(set(data['Perpetrator Race']))
    colors = sns.color_palette('Spectral')
    perpetrator_race_counts = data['Perpetrator Race'].value_counts()
    plt.pie(perpetrator_race_counts, colors=colors)
    #label title and legend
    plt.title(f'Perpetrator Race distribution in {suf}', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
    plt.legend(loc='center', labels=labels, labelcolor= 'navy')
    #I want a dont plot instead of a simple pie
    plt.gca().add_artist(plt.Circle((0,0),0.7, color='white'))
    #show the plot
    plt.show()

def plot_population_trend(data1,data2):
    # trend of the population in Texas and California from 2020 to 2014
    plt.plot(range(2000, 2015), data1[20:], color='navy', linestyle='-', label='Texas')
    plt.plot(range(2000, 2015), data2[20:], color='orchid', linestyle="-", label='California ')
    plt.title('Population Over Years', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
    plt.xlabel('Year', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':12})
    plt.ylabel('Population', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':12})
    plt.grid(True, linestyle='--', alpha=0.3, color = 'navy')
    plt.legend()
    #show the plot
    plt.show()

def plot_crimes_countries_trend(data1,data2,suf1,suf2):
    i,colors,countries = 0,['mediumaquamarine','cornflowerblue'], [suf1,suf2]
    for data in [data1,data2]:
        # distribution of crimes through the years: comparison between California and Texas
        sns.histplot(data, x='Year', hue='State', bins=35, multiple='dodge', shrink=.75, color=colors[i], kde=True, label = countries[i])
        plt.title('Crimes count: comparison between California and Texas', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
        i +=1
    # Adding grid lines
    plt.grid(True, linestyle='dotted', alpha=0.3, color = 'navy')
    #add a legend
    plt.legend(labelcolor = 'navy')
    #show the plot
    plt.show()

def plot_crimes_capitals_trend(data1,data2,suf1,suf2):
    # distribution of crimes through the years: comparison between Sacramento and Austin
    i,colors,place = 0,['mediumaquamarine','cornflowerblue'], [suf1,suf2]
    for data in [data1,data2]:
        sns.histplot(data, x='Year',
                 hue='City', bins=30, multiple='dodge', shrink=.75, color=colors[i], kde=True, label = place[i])
        plt.title('Crimes count: comparison between capitals',fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
        i+=1
    
    # Adding grid lines
    plt.grid(True, linestyle='dotted', alpha=0.3, color = 'navy')
    #add a legend
    plt.legend(labelcolor = 'navy')
    #show the plot
    plt.show()


def plot_solved_crimes(data1,data2,data3, suf1,suf2,suf3):
    #percentage of solved crimes through the years
    i,colors,place = 0,['seagreen','mediumaquamarine','cornflowerblue'], [suf1,suf2,suf3]
    for data in [data1,data2,data3]:
        solved_crimes = []
        for j in range(1980, 2015):
             solved_crimes.append(len(data[(data['Year'] == j) & (data['Crime Solved'] == 1)]) / len(data[data['Year'] == j]))
        plt.plot(range(1980, 2015), solved_crimes, color=colors[i], label=f'{place[i]}')
        i+=1
    # Adding grid lines
    plt.grid(True, linestyle='-', alpha=0.3, color = 'navy')
    #add a legend
    plt.legend(labelcolor = 'navy')
    #add title
    plt.title(f'Percentage of solved crimes', fontdict={'family':'sans',
                                               'style':'normal',
                                               'color':'navy',
                                               'weight':'normal',
                                               'size':14})
    #show the plot
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

    plot_victim_age_trend(homicide_df,homicide_California,homicide_Texas, 'US','California', 'Texas')

    plot_perpetrator_age_trend(homicide_df,homicide_California,homicide_Texas, 'US', 'California', 'Texas')

    plot_victim_race(homicide_df, 'Total')
    plot_victim_race(homicide_California, 'California')
    plot_victim_race(homicide_Texas, 'Texas')

    plot_perpetrator_race(homicide_df, 'Total')
    plot_perpetrator_race(homicide_California, 'California')
    plot_perpetrator_race(homicide_Texas, 'Texas')

    # % of homocides in capitals
    print(f'Be aware the proportion oh homicides in the capital city in respect to the entire country is very different bewteen California and Texas.',
          "The % is indeed {len(homicide_Sacramento) / len(homicide_California)} for California, while it's {len(homicide_Austin) / len(homicide_Texas)} for Texas")
    plot_population_trend(pop_tex,pop_cal)
    plot_crimes_countries_trend(homicide_California,homicide_Texas,'California','Texas')
    plot_crimes_capitals_trend(homicide_Sacramento,homicide_Austin,'Sacramento','Austin')

    plot_solved_crimes(homicide_df, homicide_California,homicide_Texas,'US','California','Texas')


if __name__ == "__main__":
    main()
