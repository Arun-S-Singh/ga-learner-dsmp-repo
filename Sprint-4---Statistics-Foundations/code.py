# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading of the file
data=pd.read_csv(path)

"""
In the column Gender, replace '-' with 'Agender' using "replace()" function. Check the distribution of Gender by ploting a graph with proper labels
"""
data['Gender'] = data['Gender'].replace('-','AGender')
sns.countplot(x=data['Gender'])

"""
Next check does good overpower evil or does evil overwhelm good? This can be done by checking the distribution of alignment through a proper chart. - Would there be any change in the majority alignment if the ones in neutral all took one side?
"""
sns.countplot(data['Alignment'])

"""
For any of the members, combat skills are really important to survive when they find themselves in unwanted situtations. Check out if combat relate to person's strength or it's intelligence? Be careful which correlation coefficient to use - Pearson's or Spearman's?
"""
fig, ax = plt.subplots(2, 3,sharex=True,figsize=(15,10))
sns.distplot(data['Combat'],ax=ax[0][0])
sns.distplot(data['Intelligence'],ax=ax[0][1])
sns.distplot(data['Strength'],ax=ax[0][2])

sns.regplot(data=data,x='Combat',y='Intelligence',ax=ax[1][0])
sns.regplot(data=data,x='Combat',y='Strength',ax=ax[1][1])

print('Correlation of Combat and Strength (Spearman)={0}'.format(data['Combat'].corr(data['Strength'],method='spearman')))

print('Correlation of Combat and Intelligence (Spearman)={0}'.format(data['Combat'].corr(data['Intelligence'],method='spearman')))


"""
Find out who are the best of the best in this superhero universe? This can be done by finding the value of quantile = 0.99 for the Total column and subset the dataframe whose Total is higher than this quantile. Create a list of the names from 'Name' associated with this subset and store in super_best_list in form of a list. These are the best of the best in the superhero universe
"""
super_best_names = list(data[data['Total'] > pd.Series(data['Total']).quantile(.99)]['Name'])
print(super_best_names)

"""
Correlation of all the vital parameters
"""
fig, ax = plt.subplots(1, 1,figsize=(5,5))
corr = data[['Intelligence','Strength','Speed','Durability','Power','Combat']].corr()

sns.heatmap(corr,annot=True,linewidths=.3,cmap='YlGnBu',ax=ax)

"""
Boxplots
"""
fig, ax = plt.subplots(3, 2,sharex=True,figsize=(5,5))

sns.boxplot(data['Intelligence'],ax=ax[0][0])
sns.boxplot(data['Strength'],ax=ax[0][1])
sns.boxplot(data['Speed'],ax=ax[1][0])
sns.boxplot(data['Durability'],ax=ax[1][1])
sns.boxplot(data['Power'],ax=ax[2][0])
sns.boxplot(data['Combat'],ax=ax[2][1])
# Code starts here



