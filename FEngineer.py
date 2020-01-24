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
        
    # 4a column with month in it:
    df['Month_'] = df['Date'].dt.month
    
    # turn Promo 2 in running on that day or not
    store_n = df
    store_n['Promo2Week_Year'] = "01.01900.0"
    store_n.loc[(store_n['Promo2SinceYear'].notna())&(store_n['Promo2SinceWeek'].notna()),'Promo2Week_Year'] = store_n['Promo2SinceWeek'].astype(str) + store_n['Promo2SinceYear'].astype(str)
    store_n['Promo2Week_Year_2'] = pd.to_datetime((store_n['Promo2Week_Year']).astype(str) + '-1', format = "%W.0%Y.0-%w")
    store_n['Promo2_running'] = 0
    store_n.loc[store_n['Promo2Week_Year_2']<store_n['Date'],'Promo2_running'] = 1
    store_n.loc[(store_n['Promo2SinceYear'].isna())&(store_n['Promo2SinceWeek'].isna()),'Promo2_running'] = 0
    store_n = store_n.drop(['Promo2Week_Year','Promo2Week_Year_2'],axis=1)
    df = store_n
    
    # 5. Some stores are open on holidays 
    df["holiday_stores"] = 0
    df.loc[(df['StateHoliday']==1) & (df['Sales'] > 0), "holiday_stores"] = 1
    # which stores are open? df[df["holiday_stores"] == 1]["Store"].unique()
    
    # 7. Sale per customer
   
    this = df.groupby(['Store', 'DayOfWeek'])['Sales'].transform('mean')
    spc = this/df["Customers"]
    spc[df["Open"] == 0] = 0
    df["SalesPerCustomer"] = spc
    
    
    
    # 8. Encoding 
    c_for_onehot = ['StateHoliday',  'PromoInterval','StoreType']#'Promo','Assortment'
    one_hot = pd.get_dummies(df[c_for_onehot])
    out = pd.concat([df, one_hot],axis = 1)
    
    # Encode stores by their average 
    out["MeanPerStore"] = df.groupby(['Store'])['Sales'].transform('mean')
    
    
    # 4b Promointerval to Months
    
    out['Promo_Month'] = 0
    out.loc[(out['PromoInterval_Feb,May,Aug,Nov']==1)&((out['Month_']==2)|(out['Month_']==5)|(out['Month_']==8)|(out['Month_']==11)), 'Promo_Month'] = 1
    out.loc[(out['PromoInterval_Jan,Apr,Jul,Oct']==1)&((out['Month_']==1)|(out['Month_']==4)|(out['Month_']==7)|(out['Month_']==10)), 'Promo_Month'] = 1
    df.loc[(out['PromoInterval_Mar,Jun,Sept,Dec']==1)&((out['Month_']==3)|(out['Month_']==6)|(out['Month_']==9)|(out['Month_']==12)), 'Promo_Month'] = 1
    
    out= out.drop('StateHoliday', axis='columns')
    #out= out.drop('Promo', axis='columns')
    out= out.drop('PromoInterval', axis='columns')
    out= out.drop('StoreType', axis='columns')
    #out= out.drop('Assortment', axis='columns')
    out = out.drop(['PromoInterval_Feb,May,Aug,Nov', 'PromoInterval_Jan,Apr,Jul,Oct','PromoInterval_Mar,Jun,Sept,Dec'], axis = 1)
    
    #Promointerval and Promo2 combined
    out['Promo2_PromoInterval'] = out['Promo']+ out['Promo2_running']
    
    #competition running now?
    out['Competition_running_help'] = "01.01900.0"
    out.loc[(out['CompetitionOpenSinceMonth'].notna())&(out['CompetitionOpenSinceYear'].notna()),'Competition_running_help'] = out['CompetitionOpenSinceMonth'].astype(str) + out['CompetitionOpenSinceYear'].astype(str)
    out['Competition_running_help2'] = pd.to_datetime((out['Competition_running_help']).astype(str) + '-1', format = "%m%Y-%w")
    
    out['Competition_running'] = 0
    out.loc[out['Competition_running_help2']<out['Date'],'Competition_running'] = 1
    out.loc[(out['CompetitionOpenSinceMonth'].isna())&(out['CompetitionOpenSinceYear'].isna()),'Competition_running'] = 0
    out = out.drop(['Competition_running_help','Competition_running_help2'],axis=1)
    
    return(out)