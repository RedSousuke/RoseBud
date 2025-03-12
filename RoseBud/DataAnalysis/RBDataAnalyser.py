from turtle import setup
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers import SKLearnRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd

import numpy as np
import pandas as pd

keras.Model.predict
# Following notebook at https://www.kaggle.com/code/sanket30/predicting-sales-using-keras-regressor/notebook
def setup(OPFILE,TARGET):
    trainingsales = pd.read_csv(OPFILE, parse_dates=['date'], date_format='mixed', dayfirst=True)
    test = pd.read_csv('DataAnalysis/test.csv')

    dataframe = trainingsales.groupby([trainingsales.date.apply(lambda x:x.strftime('%Y-%m')), 'item_id','shop_id']).sum(numeric_only=True).reset_index()
    dataframe = dataframe[['date', 'item_id', 'shop_id', 'item_cnt_day']]
    dataframe = dataframe.pivot_table(index=['item_id', 'shop_id'], columns='date', values='item_cnt_day', fill_value=0).reset_index()
    dftest = pd.merge(test, dataframe, on=['item_id', 'shop_id'], how='left').fillna(0)

    dftest = dftest.drop(labels=['ID', 'shop_id', 'item_id'], axis=1)

    global X_train, y_train
    y_train = dftest[TARGET]
    X_train = dftest.drop(labels=[TARGET], axis=1)

    global X_test
    X_test = dftest.drop(labels=['2013-01'],axis=1)
def predictSheet(file, target):
    setup(file,target)
    kmod = Sequential()
    kmod.add(Dense(64, input_dim=33, kernel_initializer='normal', activation='relu'))
    kmod.add(Dense(32, kernel_initializer='normal', activation='relu'))
    kmod.add(Dense(16, kernel_initializer='normal', activation='relu'))
    kmod.add(Dense(8, kernel_initializer='normal', activation='relu'))
    kmod.add(Dense(4, kernel_initializer='normal', activation='relu'))
    kmod.add(Dense(1, kernel_initializer='normal'))
    kmod.compile(loss='mean_squared_error', optimizer='adam')

    print("Train Start...")
    kmod.fit(X_train, y_train, epochs=100, batch_size=2000, verbose=2)
    global y_pred;
    y_pred = kmod.predict(X_test).clip(0, 20)
    y_pred = pd.DataFrame(y_pred, columns=['item_cnt_month'])
    y_pred.to_csv('output/sheets/predictions.csv', index_label='ID')
    