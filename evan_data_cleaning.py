import pandas as pd
import datetime as dt

df = pd.read_csv()

#Assortment - describes an assortment level: a = basic, b = extra, c = extended
df['Assortment'] = df['Assortment'].replace({"a": 1, "b": 2, "c": 3})


#Drop the rows where we do not have a store number
df_train = df_train.dropna(subset=['Store'])

#Convert the store numbers from float to int
df_train.loc[:, 'Store'] = df_train.loc[:, 'Store'].astype(int)

<<<<<<< HEAD
=======
#define a function
def clean_store_compyear(store):
#store Dataframe fill Competition since Year
    store = pd.read_csv("../minicomp-rossman/data/store.csv")
    store_n = store.copy()
    store_n.loc[store_n['CompetitionOpenSinceYear'].isna(),'CompetitionOpenSinceYear'] = store_n['Promo2SinceYear']
    return store_n

def clean_store_commonth(store_n):
    #store fill Competition since Month
    store_n['Promo2Week_Year'] = "01.01900.0"
    store_n.loc[(store_n['Promo2SinceYear'].notna())&(store_n['Promo2SinceWeek'].notna()),'Promo2Week_Year'] = store_n['Promo2SinceWeek'].astype(str) + store_n['Promo2SinceYear'].astype(str)
    store_n['Promo2Week_Year_2'] = pd.to_datetime((store_n['Promo2Week_Year']).astype(str) + '-1', format = "%W.0%Y.0-%w")
    store_n.loc[(store_n['CompetitionOpenSinceMonth'].isna())&(store_n['Promo2SinceWeek'].notna()),'CompetitionOpenSinceMonth'] = store_n['Promo2Week_Year_2'].dt.month
    store_n = store_n.drop(['Promo2Week_Year','Promo2Week_Year_2'],axis=1)
    return store_n

>>>>>>> 04b686db6a92d6a490838c489af1257cad58eea6

#Convert the date colume to datetime
df_train.loc[:, 'Date'] = pd.to_datetime(df_train.loc[:, 'Date'])

#Convert the DayOfWeek column to Monday(0) - Sunday(6) and replace missing values 
df_train.loc[:, 'DayOfWeek'] = df_train.loc[:, 'Date'].dt.dayofweek
<<<<<<< HEAD

#Create a numpy ns64 column
df_train["timestamp"] = df_train.Date.values.astype(np.int64)
=======
>>>>>>> 04b686db6a92d6a490838c489af1257cad58eea6
