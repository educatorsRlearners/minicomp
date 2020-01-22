import pandas as pd

df = pd.read_csv()

#Assortment - describes an assortment level: a = basic, b = extra, c = extended
df['Assortment'] = df['Assortment'].replace({"a": 1, "b": 2, "c": 3})


#Drop the rows where we do not have a store number
df_train = df_train.dropna(subset=['Store'])

#Convert the store numbers from float to int
df_train.loc[:, 'Store'] = df_train.loc[:, 'Store'].astype(int)


#Convert the date colume to datetime
df_train.loc[:, 'Date'] = pd.to_datetime(df_train.loc[:, 'Date'])

#Convert the DayOfWeek column to Monday(0) - Sunday(6) and replace missing values 
df_train.loc[:, 'DayOfWeek'] = df_train.loc[:, 'Date'].dt.dayofweek