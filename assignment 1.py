# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 20:20:42 2022

@author: Rahul Balmoor
"""
# Step 1 : Load libraries
import os 
import pandas as pd

#step 2 : Set working directory
path = 'E:/Fall 2022/python'
os.chdir(path)

a = pd.read_csv('HoustonAQIinp.csv')
type(a)

a.head(5)

a.columns = ['tottime','NOX','OZONE','BARO','RELH','DEWPT','TEMP','SRAD','WSPEED','WDIR']

aa = pd.read_csv('HoustonAQIinp.csv')
type(aa)

aa = a

aa.head(5)

WSWD = aa [['WSPEED','WDIR']]
WSWD.head()
type(WSWD)

 
 
WSWD_OZONE = aa.loc[aa['OZONE'] > 10, ['WSPEED','WDIR']]
WSWD_OZONE = aa.loc[aa['TEMP'] > 70, ['WSPEED','WDIR']]
