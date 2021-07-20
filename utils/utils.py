import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

import statsmodels.api as sm
import statsmodels.formula.api as smf

from statsmodels.stats.diagnostic import het_white
from statsmodels.compat import lzip
from patsy import dmatrices

from scipy.stats import skew, kurtosis
from itertools import product


from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt


# used to detrend
def difference(dataset, interval = 1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return np.array(diff)


def roll_window(dataset, win_size, func):
    return dataset.rolling(int(win_size), center=True).apply(func)

def do_ews_std(dataset, time, win_size):
    return dataset.rolling(int(win_size), center=True).std()

def do_ews_skew(dataset, time, win_size):
    return dataset.rolling(int(win_size)).apply(skew)

def do_ews_kurt(dataset, time, win_size):
    return dataset.rolling(int(win_size)).apply(kurtosis)

def get_auto(dataset, lag=1):
    return sm.tsa.acf(dataset)[lag]

def do_ews_auto(dataset, time, win_size, lag=1):
    return dataset.rolling(int(win_size)).apply(get_auto)

def get_ch(dataset, time):
    df = pd.DataFrame(dataset)
    df['Time'] = time.loc[dataset.index]
    df[f'LOG_'] = np.log(dataset)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.dropna()
    expr = f'LOG_ ~ Time'
    y, X = dmatrices(expr, df, return_type='dataframe')
    olsr_results = smf.ols(expr, df).fit()
    keys = ['Lagrange Multiplier statistic:', 'LM test\'s p-value:', 'F-statistic:', 'F-test\'s p-value:']
    results = het_white(olsr_results.resid, X)
#     lzip(keys, results)
    return results[1]

def do_ews_ch(dataset, time, win_size):
    return dataset.rolling(int(win_size)).apply(get_ch, args =(time,) )

def do_ar(dataset, lag=1):
    model = AutoReg(dataset, lags=lag)
    model_fit = model.fit()
    return model_fit.params[1]

def do_ews_ar(dataset, time, win_size, lag=1):
    return dataset.rolling(int(win_size)).apply(do_ar)

