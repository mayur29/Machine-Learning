# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:01:44 2018

@author: M61958
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

print("Train data dimensions: ", train_data.shape)
print("Test data dimensions: ", test_data.shape)