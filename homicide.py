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