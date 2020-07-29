# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Loading the data
data=pd.read_csv(path)

#Code starts here

#Rating>5
data = data[ data['Rating'] <= 5]

#distribution of app ratings
sns.distplot(data['Rating'])

# Check for nulls in data
print(data.isnull().sum())

# Treat - Drop the rows with NAN
data = data.dropna(axis=0)


#Genre
Genres = data['Genres'].unique()
print(Genres)

data['Genres'] = data['Genres'].apply(lambda row: str(row).split(';')[0])

Genres = data['Genres'].unique()
print(Genres)

# Highest/Lowest rating by Genres
grouped = data.groupby('Genres')['Rating'].mean().sort_values(ascending=False)
highest_rating = grouped[0]
lowest_rating = grouped[-1]

# Clean Installs and Price
data['Installs'] = data['Installs'].replace(',','')
data['Price'] = data['Price'].replace('$','')

#Update last updated column
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

















