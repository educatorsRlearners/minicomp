from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import xgboost as xgb
#from xgboost import XGBRegressor

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def split_train_valid(train_clean):
    #insert dataframe
    X = train_clean.drop('Sales',axis = 1)
    y = train_clean['Sales']

    #idx_sep = int(train_clean.shape[0]*(2/3))
    #X_train = X[:idx_sep]
    #X_test = X[idx_sep:]
    #y_train = y[:idx_sep]
    #y_test = y[idx_sep:]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    return X_train, X_test, y_train, y_test

#def rmse(y_true, y_pred):#
#
#    result = np.sqrt((((y_true-y_pred)/y_true)**2).sum()/y_true.shape[0])#

#    return result


def rmse(actuals,preds):
    preds = preds.reshape(-1)
    actuals = actuals.reshape(-1)
    assert preds.shape == actuals.shape
    return 100 * np.linalg.norm((actuals - preds) / actuals) / np.sqrt(preds.shape[0])

#from sklearn.ensemble import RandomForestRegressor
def rfm_fit(X_train, X_test, y_train, y_test, n_estimators, max_depth, max_features):
    rfr = RandomForestRegressor(n_jobs = -1, verbose = 1, n_estimators=n_estimators, max_depth=max_depth, max_features=max_features)
    rfr.fit(X_train,y_train)
    prediction = rfr.predict(X_test)
    prediction_train = rfr.predict(X_train)
    return rfr, prediction, prediction_train 


def xgboost(X_train, X_test, y_train, y_test, n_estimators,max_depth, max_features):
    xg_reg = xgb.XGBRegressor(n_jobs = -1, verbosity = 1,n_estimators=n_estimators, max_depth=max_depth, max_features=max_features)
    
    xg_reg.fit(X_train,y_train)

    preds = xg_reg.predict(X_test)
    preds_train = xg_reg.predict(X_train)

    return xg_reg, preds, preds_train

    
    
def plot_feature_importances(rf, cols, model_dir):
    importances = pd.DataFrame()
    importances.loc[:, 'importances'] = rf.feature_importances_
    importances.loc[:, 'features'] = cols
    importances.sort_values('importances', inplace=True)
    f, a = plt.subplots()
    importances.plot(ax=a, kind='bar', x='features', y='importances')
    plt.gcf().subplots_adjust(bottom=0.3)
    f.savefig(os.path.join(model_dir, 'importances.png'))
    
#from sklearn.ensemble import RandomForestRegressor
#import xgboost as xgb
#from sklearn.model_selection import GridSearchCV
#from sklearn.metrics.scorer import make_scorer
#rf = RandomForestRegressor(n_jobs = -1)
#xb = xgb.XGBRegressor(n_jobs = -1)

#n_estimators = [10, 50]#, 100, 150]
#max_depth = [10, 50]# ,100, 150]
#max_features = [10,20,29]
#min_samples_leaf = [1,3,5]

#my_scorer = make_scorer(rfm.rmse, greater_is_better=False)
"""
grid = GridSearchCV(estimator=rf, cv=3, scoring = my_scorer,
                    param_grid=dict(n_estimators=n_estimators, max_depth=max_depth, 
                                      max_features=max_features,min_samples_leaf=min_samples_leaf))
"""
#grid.fit(X_train.values, y_train.values)
#print (grid.best_score_)
#print (grid.best_params_)
    




#xgboost
#max features sqrt(len(X.columns), max depth, max trees 500-1000
#cross validation
#feature importances -> 
#grid search
#random search
#manually search
#basyian hyperp optimization
#FE: promo1 +2: ands and nots


