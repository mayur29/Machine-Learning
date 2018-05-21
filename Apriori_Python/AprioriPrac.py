# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:07:29 2018

@author: M61958
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transations = []
for i in range(0,7501):
    transations.append([str(dataset.values[i,j]) for j in range (0,20)])
    
from apyori import apriori

    