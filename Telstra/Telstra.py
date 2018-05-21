# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:58:23 2018

@author: M61958
"""

import pandas as pd
import numpy as np
import matplotlib as plt

df= pd.read_csv('test.csv')
df['source'] = 'test'

dt= pd.read_csv('train.csv')
dt['source'] = 'train'

data = pd.concat([df, dt])

count = data['id'].unique


