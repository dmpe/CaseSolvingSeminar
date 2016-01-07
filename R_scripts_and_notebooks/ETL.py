# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:56:11 2015

@author: jm
"""
import pandas as pd

data = pd.read_csv("data.csv", parse_dates=True, infer_datetime_format=True, 
            sep = None, encoding = "latin-1")
            
            
data.head()            
print(data)
