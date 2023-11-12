import pandas as pd
import seaborn as sns
import matplotlib
print(matplotlib.get_backend())
matplotlib.use('TkAgg')  # Or another backend suitable for your environment
import matplotlib.pyplot as plt
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
homicide_California['Crime Solved'] = homicide_California['Crime Solved'].replace({'Yes': 1, 'No': 0})
homicide_Texas['Crime Solved'] = homicide_Texas['Crime Solved'].replace({'Yes': 1, 'No': 0})
#it's not necessary to change the type to interepret the regression eventually

set(homicide_df['Victim Sex'])
#for now we do not convert into dummies as we want to keep this particular variable as categorical for the EDA

set(homicide_df['Victim Age'])
#here we have outliers: (age 998) !! We then decided to delete that row
homicide_df = homicide_df[homicide_df['Victim Age']!= 998]
plt.figure(figsize=(8, 6))
homicide_df_sorted = homicide_df.sort_values(by=['Victim Age'])
sns.lineplot(data=homicide_df, x='Year', y='Victim Age', hue='State', palette=['orchid', 'navy'], marker='x', linestyle = '--')
plt.title('Victim Age trend')
plt.show()

set(homicide_California['Perpetrator Sex'])
#for now we do not convert into dummies as we want to keep this particular variable as categorical for the EDA

set(homicide_California['Perpetrator Age'])
#outliers 95/05 : per Edo
homicide_df = homicide_df[homicide_df['Perpetrator Age']!= 0]
plt.figure(figsize=(8, 6))
homicide_df_sorted = homicide_df.sort_values(by=['Perpetrator Age'])
sns.lineplot(data=homicide_df, x='Year', y='Perpetrator Age', hue='State', palette=['orchid', 'navy'], marker='o')
plt.title('Perpetrator Age trend')
plt.show()

set(homicide_California['Perpetrator Race'])
set(homicide_California['Perpetrator Ethnicity'])
#{'Asian/Pacific Islander', 'White', 'Black', 'Native American/Alaska Native', 'Unknown'}

#PARTE DI EDO: ARMI
set(homicide_California['Weapon'])
#{'Drugs', 'Firearm', 'Fire', 'Rifle', 'Explosives', 'Poison', 'Blunt Object', 'Gun', 'Shotgun', 'Unknown', 'Suffocation', 'Drowning', 'Strangulation', 'Knife', 'Handgun'}

#EDA
#population in Texas and California: extention of the research
population = pd.read_csv('population_usafacts.csv')
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
plt.plot(range(2000,2015), pop_tex[20:],color = 'navy',linestyle='--' , label = 'Texas')
plt.plot(range(2000, 2015), pop_cal[20:], color = 'orchid', linestyle ="--" ,label = 'California ')
plt.title('Population Over Years')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()

#% of homocides in capitals
len(homicide_Sacramento)/len(homicide_California)
len(homicide_Austin)/len(homicide_Texas)

#EDA about victim race
# Victim race distribution overall
labels = set(homicide_California['Victim Race'])
colors = ['dimgrey', 'brown', 'snow', 'burlywood', 'turquoise']

victim_race_counts = homicide_df['Victim Race'].value_counts()
plt.pie(victim_race_counts, colors = colors, shadow = True, startangle = 140 )
plt.title('Victim Race overall distribution')
plt.legend(title = 'Races', loc = 'lower center',labels = labels)
plt.show()
#victim race distribution in California
victim_race_counts_California = homicide_California['Victim Race'].value_counts()
plt.pie(victim_race_counts_California, colors=colors, shadow=True, startangle=140)
plt.title('Victim Race in California')
plt.legend(title = 'Races', loc = 'lower center', labels = labels)
plt.show()
#victim race distribution in Texas
victim_race_counts_Texas = homicide_Texas['Victim Race'].value_counts()
plt.pie(victim_race_counts_Texas, colors = colors, shadow = True, startangle=140)
plt.title('Victim Race in Texas')
plt.legend(title = 'Races', loc = 'lower center',labels = labels)
plt.show()

#EDA about perpetrator race
# Perpetrator race distribution overall
perpetrator_race_counts = homicide_df['Perpetrator Race'].value_counts()
plt.pie(perpetrator_race_counts, colors = colors)
plt.title('Perpetrator Race overall distribution')
plt.legend(title = 'Races', loc = 'upper center', labels =labels)
plt.show()
#perpetrator race distribution in California
perpetrator_race_counts_cal = homicide_California['Perpetrator Race'].value_counts()
plt.pie(perpetrator_race_counts_cal, colors = colors)
plt.title('Perpetrator Race in California')
plt.legend(title = 'Races', loc = 'upper center', labels = labels)
plt.show()
#perpetrator race distribution in Texas
perpetrator_race_counts_tex = homicide_Texas['Perpetrator Race'].value_counts()
plt.pie(perpetrator_race_counts_tex, colors = colors)
plt.title('Perpetrator Race in Texas')
plt.legend(title = 'Races', loc = 'upper center', labels = labels)
plt.show()


#distribution of crimes through the years: comparison between California and Texas
sns.histplot(homicide_df, x = 'Year', hue = 'State', bins = 35,  multiple='dodge', shrink=.75, palette = ['orchid','navy'])
plt.figure(figsize=(8, 6))
plt.show()
#distribution of crimes through the years: comparison between capitals
sns.histplot(homicide_df[(homicide_df['City']=='Austin') | (homicide_df['City']=='Sacramento')], x = 'Year', hue = 'City', bins = 30,  multiple='dodge', shrink=.75)
plt.figure(figsize=(8, 6))
plt.title('Crimes count')
plt.show()

def remove_outliers_95_05(data, column_name):
    """
    Remove outliers from a pandas DataFrame based on the 5th and 95th percentiles.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column from which to remove outliers.

    Returns:
    pd.DataFrame: A DataFrame with outliers removed.
    """

    lower_percentile = data[column_name].quantile(0.05)
    upper_percentile = data[column_name].quantile(0.95)

    filtered_data = data[(data[column_name] >= lower_percentile) & (data[column_name] <= upper_percentile)]
    return filtered_data

homicide_df['Perpetrator Age'] = pd.to_numeric(homicide_df['Perpetrator Age'], errors='coerce')
filtered_data = remove_outliers_95_05(homicide_df, 'Perpetrator Age')

#percentage of solved crimes through the years
solved_crimes = []
for i in list(set(homicide_df['Year'])):
    solved_crimes.append(len(homicide_df[(homicide_df['Year']==i) &(homicide_df['Crime Solved']==1)])/len(homicide_df[homicide_df['Year']==i]))
solved_crimes_cal = []
for i in list(set(homicide_California['Year'])):
    solved_crimes_cal.append(len(homicide_California
                             [(homicide_California
                                          ['Year']==i) &(homicide_California['Crime Solved']==1)])/len(homicide_California[homicide_California['Year']==i]))
solved_crimes_tex = []
for i in list(set(homicide_Texas['Year'])):
    solved_crimes_tex.append(len(homicide_Texas
                             [(homicide_Texas
                                          ['Year']==i) &(homicide_Texas['Crime Solved']==1)])/len(homicide_Texas[homicide_Texas['Year']==i]))
plt.plot(range(1980,2015), solved_crimes, color = 'peachpuff', label = 'generic')
plt.plot(range(1980,2015), solved_crimes_cal, color = 'orchid',label = 'California' )
plt.plot(range(1980,2015), solved_crimes_tex, color = 'navy', label = 'Texas')
plt.legend()
plt.show()


#DATA ANALYSIS
#does the perpetrator age affect the amount on unsolved crimes? NOT WORKING HERE!!
plt.figure(figsize=(8, 6))
homicide_df = homicide_df[homicide_df['Perpetrator Age']!=0]
homicide_df.groupby('Perpetrator Age')
sns.countplot(x='Perpetrator Age', hue='Crime Solved', data=homicide_df, palette=['lightgreen', 'salmon'])
plt.title('Distribution of Solved and Unsolved Crimes by Perpetrator Age')
plt.xlabel('Perpetrator Age')
plt.ylabel('Count')
plt.legend(['solved', 'unsolved'])
plt.show()