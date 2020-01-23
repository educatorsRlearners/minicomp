import pandas as pd
import numpy as np

def clean_store(df):
    df['Assortment'] = df['Assortment'].replace({"a": 1, "b": 2, "c": 3})
    #Fill missing values from CopetitionDistance with the Mode
    df.CompetitionDistance = df.CompetitionDistance.fillna(250)
    #Impute missing values
    df.CompetitionOpenSinceYear = df.CompetitionOpenSinceYear.fillna(2013)
    df.CompetitionOpenSinceMonth = df.CompetitionOpenSinceMonth.fillna(9)
    #Convert to integers
    df[['CompetitionOpenSinceMonth','CompetitionOpenSinceYear']] = df[['CompetitionOpenSinceMonth','CompetitionOpenSinceYear']] .astype(int)
    return df

#clean_store(df)

def clean_train(train):
    '''Clean the data from the train set'''
    #Drop the rows where we do not have a store number
    #train = pd.read_csv("../minicomp-rossman/data/train.csv")
    train = train.dropna(subset=['Store'])
    #Convert the store numbers from float to int
    train.loc[:, 'Store'] = train.loc[:, 'Store'].astype(int)
    #Convert the date colume to datetime
    train.loc[:, 'Date'] = pd.to_datetime(train.loc[:, 'Date'])
    #Convert the DayOfWeek column to Monday(0) - Sunday(6) and replace missing values 
    train.loc[:, 'DayOfWeek'] = train.loc[:, 'Date'].dt.dayofweek
    #Convert to a timestamp
    train["timestamp"] = train.Date.values.astype(np.int64)
    #Remove rows where we do not have a vale for sales or customers
    train = train[(train["Sales"].notna()) | (train["Customers"].notna())]
    return train

def store_train_merge(df, train):
    #Merge the tables
    master = train.merge(df, left_on="Store", right_on="Store")
    return master