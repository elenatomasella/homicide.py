import pandas as pd
#import the dataset
homicide = pd.read_csv("database.csv", low_memory = False)
homicide_df= pd.DataFrame(homicide)
#reduction of the dataset
print(homicide_df.columns)
homicide_df = homicide_df[['City', 'State', 'Year', 'Month', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age','Victim Race', 'Perpetrator Sex','Perpetrator Age','Perpetrator Race','Perpetrator Ethnicity', 'Weapon', 'Relationship']]
homicide_df= homicide_df[homicide_df['State'].isin(['Texas','California'])]
#specific datasets we extract to get insights via comparisons
homicide_Texas = homicide_df[homicide_df['State']=='Texas']
homicide_California =homicide_df[homicide_df['State']=='California']
homicide_Austin = homicide_df[homicide_df['City']=='Austin']
homicide_Sacramento = homicide_df[homicide_df['City']=='Sacramento']

print(homicide_df.describe().T)
homicide_df.info
#necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

#check for na values in the dataframe
print(homicide_df.isnull().values.any())

#view the clean dataset -partially
homicide_df.describe()

#continue data-cleaning
#for now we have two numerical variables only so we need to convert the other ones properly
homicide_df.columns
set(homicide_df['Crime Type'])
#{'Manslaughter by Negligence', 'Murder or Manslaughter'}
homicide_df['Crime Type'] = homicide_df['Crime Type'].replace({'Murder or Manslaughter': 1, 'Manslaughter by Negligence': 0})
#it's not necessary to change the type to interepret the regression eventually
homicide_df = homicide_df.rename(columns={'Crime Type': 'Crime Type: intentional manslaughter?'})

set(homicide_df['Crime Solved'])
homicide_df['Crime Solved'] = homicide_df['Crime Solved'].replace({'Yes': 1, 'No': 0})
#it's not necessary to change the type to interepret the regression eventually

set(homicide_df['Victim Sex'])
#for now we do not convert into dummies as we want to keep this particular variable as categorical for the EDA

set(homicide_df['Victim Age'])
#here we have outliers: (age 998) !! We then decided to delete that row
homicide_df = homicide_df[homicide_df['Victim Age']!= 998]

set(homicide_California['Perpetrator Sex'])
#for now we do not convert into dummies as we want to keep this particular variable as categorical for the EDA

set(homicide_California['Perpetrator Age'])
#outliers 95/05 : per Edo

set(homicide_California['Perpetrator Race'])
set(homicide_California['Perpetrator Ethnicity'])
#{'Asian/Pacific Islander', 'White', 'Black', 'Native American/Alaska Native', 'Unknown'}

#PARTE DI EDO: ARMI
set(homicide_California['Weapon'])
#{'Drugs', 'Firearm', 'Fire', 'Rifle', 'Explosives', 'Poison', 'Blunt Object', 'Gun', 'Shotgun', 'Unknown', 'Suffocation', 'Drowning', 'Strangulation', 'Knife', 'Handgun'}

#EDA
#population in Texas and California: extention of the research
population = pd.read_csv('population_usafacts.csv')
type(population)
#population US
pop = []
for i in range(1980,2015):
    pop.append(population[f'{i}'][0])
#population California
pop_cal = []
for i in range(81, 116):
    pop_cal.append(population.iloc[25, i])
#population Texas:
pop_tex = []
for i in range(81, 116):
    pop_tex.append(population.iloc[64, i])
#trend of the population in Texas and California from 2020 to 2014
plt.plot(range(2000,2015), pop_tex[20:],color = 'blue', label = 'Texas')
plt.plot(range(2000, 2015), pop_cal[20:], color = 'seagreen', label = 'California ')
plt.title('Population Over Years')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()

# Victim race distribution overall
import matplotlib.pyplot as plt
victim_race_counts = homicide_df['Victim Race'].value_counts()
plt.pie(victim_race_counts)
plt.title('Victim Race overall distribution')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_df['Victim Race']))
plt.show()
#victim race distribution in California
victim_race_counts_California = homicide_California['Victim Race'].value_counts()
plt.pie(victim_race_counts_California)
plt.title('Victim Race in California')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_California['Victim Race']))
plt.show()
#victim race distribution in Texas
victim_race_counts_Texas = homicide_Texas['Victim Race'].value_counts()
plt.pie(victim_race_counts_Texas)
plt.title('Victim Race in Texas')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_Texas['Victim Race']))
plt.show()

#EDA about perpetrator race
# Perpetrator race distribution overall
import matplotlib.pyplot as plt
perpetrator_race_counts = homicide_df['Perpetrator Race'].value_counts()
plt.pie(perpetrator_race_counts)
plt.title('Perpetrator Race overall distribution')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_df['Perpetrator Race']))
plt.show()
#perpetrator race distribution in California
perpetrator_race_counts_cal = homicide_California['Perpetrator Race'].value_counts()
plt.pie(perpetrator_race_counts_cal)
plt.title('Perpetrator Race in California')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_df['Perpetrator Race']))
plt.show()
#victim race distribution in Texas
perpetrator_race_counts_tex = homicide_Texas['Perpetrator Race'].value_counts()
plt.pie(perpetrator_race_counts_tex)
plt.title('Perpetrator Race in Texas')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_Texas['Perpetrator Race']))
plt.show()
#distribution od crimes through the years: comparison between California and Texas
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(homicide_df, x = 'Year', hue = 'State', bins = 35,  multiple='dodge', shrink=.75)
plt.figure(figsize=(8, 6))
plt.show()

#distribution od crimes through the years: comparison between capitals
sns.histplot(homicide_df[(homicide_df['City']=='Austin') | (homicide_df['City']=='Sacramento')], x = 'Year', hue = 'City', bins = 30,  multiple='dodge', shrink=.75)
plt.figure(figsize=(8, 6))
plt.show()

#percentage of solved crimes through the years
solved_crimes = []
for i in list(set(homicide_df['Year'])):
    solved_crimes.append(len(homicide_df[(homicide_df['Year']==i) &(homicide_df['Crime Solved']==1)])/len(homicide_df[homicide_df['Year']==i]))
solved_crimes_cal = []
for i in list(set(homicide_California['Year'])):
    solved_crimes_cal.append(len(homicide_California
                             [(homicide_California
                                          ['Year']==i) &(homicide_California['Crime Solved']=='Yes')])/len(homicide_California[homicide_California['Year']==i]))
solved_crimes_tex = []
for i in list(set(homicide_Texas['Year'])):
    solved_crimes_tex.append(len(homicide_Texas
                             [(homicide_Texas
                                          ['Year']==i) &(homicide_Texas['Crime Solved']=='Yes')])/len(homicide_Texas[homicide_Texas['Year']==i]))
import matplotlib.pyplot as plt
plt.plot(range(1980,2015), solved_crimes, color = 'blue', label = 'generic')
plt.plot(range(1980,2015), solved_crimes_cal, color = 'red',label = 'California' )
plt.plot(range(1980,2015), solved_crimes_tex, color = 'green', label = 'Texas')
plt.legend()
plt.show()

#population analysis
len(homicide_Sacramento)/len(homicide_California)
len(homicide_Austin)/len(homicide_Texas)
