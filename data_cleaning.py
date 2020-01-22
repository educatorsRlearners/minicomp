import pandas as pd

df = pd.read_csv()

#Assortment - describes an assortment level: a = basic, b = extra, c = extended
df['Assortment'] = df['Assortment'].replace({"a": 1, "b": 2, "c": 3})


#Drop the rows where we do not have a store number
df_train = df_train.dropna(subset=['Store'])

#Convert the store numbers from float to int
df_train.loc[:, 'Store'] = df_train.loc[:, 'Store'].astype(int)

#define a function
store = pd.read_csv("../minicomp-rossman/data/store.csv")
store.loc[store_n['CompetitionOpenSinceYear'].isna(),'CompetitionOpenSinceYear'] = store['Promo2SinceYear']
