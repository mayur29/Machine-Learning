# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:47:59 2018

@author: M61958
"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

tips = pd.read_csv('tips.csv')
sns.lmplot(x='total_bill' , y ='tip' , data = tips , hue= 'sex' , palette='Set1')
sns.lmplot(x='total_bill' , y ='tip' , data = tips , col = 'sex')
