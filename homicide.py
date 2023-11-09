import pandas as pd
#import the dataset
homicide = pd.read_csv("database.csv", low_memory = False)
homicide_df= pd.DataFrame(homicide)
#reduction of the dataset
print(homicide_df.columns)
homicide_df = homicide_df[['City', 'State', 'Year', 'Month', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age',
                           'Victim Race', 'Perpetrator Sex','Perpetrator Age','Perpetrator Race','Perpetrator Ethnicity', 'Weapon', 'Victim Count','Perpetrator Count']]
#specific datasets we extract to get insights via comparisons
homicide_Texas = homicide_df[homicide_df['State']=='Texas']
homicide_California =homicide_df[homicide_df['State']=='California']
homicide_Austin = homicide_df[homicide_df['City']=='Austin']
homicide_Sacramento = homicide_df[homicide_df['City']=='Sacramento']

print(homicide_df.describe().T)

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
homicide_df = homicide_df.rename(columns={'Crime Type': 'Crime Type: intentional manslaughter?'})

set(homicide_df['Crime Solved'])
#convertions into a dummy variable
homicide_df['Crime Solved'] = homicide_df['Crime Solved'].replace({'Yes': 1, 'No': 0})

set(homicide_df['Victim Sex'])

set(homicide_df['Victim Age'])
#here we have outliers (age 998) !!
homicide_df = homicide_df[homicide_df['Victim Age']!= 998]

set(homicide_California['Perpetrator Sex'])
set(homicide_California['Perpetrator Age'])
set(homicide_California['Perpetrator Race'])
set(homicide_California['Perpetrator Ethnicity'])
#{'Asian/Pacific Islander', 'White', 'Black', 'Native American/Alaska Native', 'Unknown'}
set(homicide_California['Weapon'])
#{'Asian/Pacific Islander', 'White', 'Black', 'Native American/Alaska Native', 'Unknown'}

#EDA
# Victim race distribution overall
victim_race_counts = homicide_df['Victim Race'].value_counts()
plt.pie(victim_race_counts)
plt.title('Victim Race overall distribution')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_df['Victim Race']))
plt.show()
#victim race distribution in California
victim_race_counts_California = homicide_California['Victim Race'].value_counts()
plt.pie(victim_race_counts)
plt.title('Victim Race in California')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_California['Victim Race']))
plt.show()
#victim race distribution in Texas
victim_race_counts_Texas = homicide_Texas['Victim Race'].value_counts()
plt.pie(victim_race_counts)
plt.title('Victim Race in Texas')
plt.legend(title = 'Races', loc = 'upper center', labels = set(homicide_Texas['Victim Race']))
plt.show()

#distribution od crimes through the years: comparison between California and Texas
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
plt.plot(range(1980,2015), solved_crimes, color = 'blue')
plt.plot(range(1980,2015), solved_crimes_cal, color = 'red')
plt.plot(range(1980,2015), solved_crimes_tex, color = 'green')
plt.show()
