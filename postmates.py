"""
Created on Wed Nov 18 07:04:49 2020
Used to analyze postmates courier data for Zeng.


@author: JSNZE
"""

"""
LinearRegression()
"""
import pandas as pd
import numpy as np
from scipy import stats
# It has to be used as lr() do set it as a object instead of a variable
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt  # To visualize
import statsmodels.api as sm
import datetime

"""
Import data into postmates as a dataframe.
"""
file='postmates.csv'
og=pd.read_csv(file)

"""
Formatting the dataframe
"""
og["wday"]=pd.to_datetime(og["doff"]).dt.dayofweek
og["wdaybool"]=0
og.loc[og["wday"]>4, "wdaybool"] = 1
ox=og[["pay", "tip", "wdaybool"]]

"""
Selecting only a specific column from the pandas file into a numpy array. In this sense it's the first two columsn'
 dir(), vars() or the inspect

"""
w=og.to_numpy()
X = og.iloc[:, 0].values.reshape(-1, 1)  
Y = og.iloc[:, 1].values.reshape(-1, 1) 
z=lr().fit(X, Y)
vars(z)

"""
Do the same thing as above, but in one line using the function lr().fit(X, Y)
"""

vars(lr().fit(np.reshape(w[:,0], (-1,1)), np.reshape(w[:,1], (-1,1))))

"""
Table of simple correlation
"""

def function_correls1(og):
    dfx=og[["pay","tip", "fast", "wday", "wdaybool"]]
    df_corr = pd.DataFrame() # Correlation matrix
    df_p = pd.DataFrame()  # Matrix of p-values
    for x in dfx.columns:
        for y in dfx.columns:
            corr = stats.pearsonr(dfx[x], dfx[y])
            df_corr.loc[x,y] = corr[0]
            df_p.loc[x,y] = corr[1]
   # print(df_corr)
   # print(df_p)
    return[df_corr,df_p]




stats.pearsonr(og["tip"], og["pay"])
# (Correlation, P-value)
stats.ttest_ind(ox["tip"], ox["pay"])
# (T-score, equivalence in p-value)
"""
#
some scripts to use.

stats.f_oneway(ox.loc[ox["wdaybool"]==1, "tip"], ox.loc[ox["wdaybool"]==0,"tip"])
stats.ttest_ind(ox.loc[ox["wdaybool"]==1, "tip"], ox.loc[ox["wdaybool"]==0,"tip"])





stats.f_oneway(og.loc[og["wday"]==1, "pay"], og.loc[og["wday"]==0,"pay"], 
               og.loc[og["wday"]==2,"pay"], og.loc[og["wday"]==5,"pay"]
               , og.loc[og["wday"]==3,"pay"], og.loc[og["wday"]==6,"pay"]
               , og.loc[og["wday"]==4,"pay"])












"""