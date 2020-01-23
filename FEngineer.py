# function takes in dataframe and creates new columns. function outputs manipulated df with additional columns
# requires JOINed Store and Train data 

## DO ONE HOT ENCODING AT THE END 
import pandas as pd

def FEngineer(df):
  
    # 1. # number of consecutive closed days prior to this day, cap at 4 or 5 
    # apply on a per-store level - unless  all shops closed on the same days? 
    df = df.sort_values(['Store', 'Date'])
    
    # convert a's to 1, b's to 2, in order to be able to use max for lag
    df["StateHoliday"] = df["StateHoliday"].replace(to_replace="a", value=1 ) 
    df["StateHoliday"] = df["StateHoliday"].replace(to_replace="b", value=2 ) 
    df["StateHoliday"] = df["StateHoliday"].replace(to_replace="c", value=3 ) 

    shift_one = df["StateHoliday"].shift(1)
    shift_one.fillna(0, inplace=True)
    shift_one = shift_one.astype(int)

    shift_two = df["StateHoliday"].shift(2)
    shift_two.fillna(0, inplace=True)
    shift_two = shift_two.astype(int)

    After_hols = pd.concat([shift_one, shift_two], axis=1).max(axis=1)
    df["Afer_hols"] = After_hols
    
    # 2. #  flag of days of end of promo OR number of days that promo is over (shift 2)
    
    # 1. # number of consecutive closed days prior to this day, cap at 4 or 5 
    # apply on a per-store level - unless  all shops closed on the same days? 
    df = df.sort_values(['Store', 'Date'])
    
    # convert a's to 1, b's to 2, in order to be able to use max for lag
    shift_one = df["Promo2"].shift(1)
    shift_one.fillna(0, inplace=True)
    
    shift_two = df["Promo2"].shift(2)
    shift_two.fillna(0, inplace=True)

    After_promo = pd.concat([shift_one, shift_two], axis=1).max(axis=1)
    df["After_promo"] = After_promo
    
    # apply on a per-store level
    # use sth like  a.x2 = a.x2.shift(1)
    
    # 3. trend over time per store
    #  ["Sales"].rolling(window=50).mean()
    
    # 4. How many months was the competition in place for? 
        # not necessary, since we are always looking at the same timeframe.
        # but maybe we need to bin it 
    
    # 5. Some stores are open on holidays 
    df["holiday_stores"] = 0
    df.loc[(df['StateHoliday']==1) & (df['Sales'] > 0), "holiday_stores"] = 1
    # which stores are open? df[df["holiday_stores"] == 1]["Store"].unique()
    
    # 7. Sale per customer
    df["SalesPerCustomer"]  = df["Sales"]/df["Customers"]
    
    # 8. Encoding 
    c_for_onehot = ['StateHoliday', 'Promo', 'PromoInterval','StoreType']
    one_hot = pd.get_dummies(df[c_for_onehot])
    out = pd.concat([df, one_hot],axis = 1)
    
    # Encode stores by their average 
    out["MeanPerStore"] = df.groupby(['Store'])['Sales'].transform('mean')
    
    # dropc_for_onehot
    
    out= out.drop('StateHoliday', axis='columns')
    out= out.drop('Promo', axis='columns')
    out= out.drop('PromoInterval', axis='columns')
    out= out.drop('StoreType', axis='columns')
    
    return(df)