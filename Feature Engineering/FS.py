# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:19:05 2018

@author: M61958
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.stats as spstats

# =============================================================================
# poke_df = pd.read_csv('Pokemon.csv', encoding='utf-8')
# poke_df[['HP', 'Attack', 'Defense']].head()
# poke_df[['HP', 'Attack', 'Defense']].describe()
# 
# df = pd.DataFrame()
# df['A'] = [1,2,3,4]
# 
# fcc_survey_df = pd.read_csv('2016-FCC-New-Coders-Survey-Data.csv', encoding='utf-8')
# fcc_survey_df[['ID.x', 'EmploymentField', 'Age', 'Income']].head()
# 
# fig , ax = plt.subplots()
# fcc_survey_df['Age'].hist(color = 'Red' , edgecolor = 'Black')
# ax.set_title('Developer Age Histogram', fontsize=12)
# ax.set_xlabel('Age', fontsize=12)
# ax.set_ylabel('Frequency', fontsize=12)
# 
# fcc_survey_df['Age_bin_round'] = np.array(np.floor(np.array(fcc_survey_df['Age']/10)))
# fcc_survey_df[['ID.x' , 'Age' ,'Age_bin_round']].iloc[1071:1076]    
# 
# # =============================================================================
# # Age Range : Bin
# # ---------------
# #  0 -  15  : 1
# # 16 -  30  : 2
# # 31 -  45  : 3
# # 46 -  60  : 4
# # 61 -  75  : 5
# # 75 - 100  : 6
# # =============================================================================
# 
# bin_ranges = [0, 15, 30, 45, 60, 75, 100]
# bin_names = [1, 2, 3, 4, 5, 6]
# 
# fcc_survey_df['Age_bin_custom_range'] = pd.cut( np.array (fcc_survey_df['Age']), bins = bin_ranges)
# 
# fcc_survey_df['Age_bin_custom_label'] = pd.cut(np.array(fcc_survey_df['Age']),  bins=bin_ranges,labels=bin_names)
# 
# 
# fcc_survey_df[['ID.x', 'Age', 'Age_bin_round', 'Age_bin_custom_range', 'Age_bin_custom_label']].iloc[1071:1076]
# 
# fig , ax = plt.subplots()
# fcc_survey_df['Income'].hist(color = 'Red' , edgecolor = 'Black')
# 
# quantile_list = [0.25,0.5,0.75,1.0]
# quantitles = fcc_survey_df['Income'].quantile(quantile_list)
# 
# for quantile in quantiles:
#     qvl = plt.axvline(quantile , color ='r')
#     
# ax.legend([qvl], ['Quantiles'], fontsize=10)
# ax.set_title('Developer Income Histogram with Quantiles', 
#              fontsize=12)
# ax.set_xlabel('Developer Income', fontsize=12)
# ax.set_ylabel('Frequency', fontsize=12)
# 
# =============================================================================
# =============================================================================
# 
# 
# vg_df = pd.read_csv('vgsales.csv', encoding='utf-8')
# vg_df[['Name', 'Platform', 'Year', 'Genre', 'Publisher']].iloc[1:7]
# 
# genres = np.unique(vg_df['Genre'])
# 
# from sklearn.preprocessing import LabelEncoder
# gle = LabelEncoder()
# genre_labels = gle.fit_transform(vg_df['Genre'])
# vg_df['GenreLabel'] = genre_labels
# 
# poke_df = pd.read_csv('Pokemon.csv', encoding='utf-8')
# 
# poke_df = poke_df.sample( random_state=1,frac=1 ).reset_index(drop=True)
# 
# gen_ord_map = {'Gen 1': 1, 'Gen 2': 2, 'Gen 3': 3, 'Gen 4': 4, 'Gen 5': 5, 'Gen 6': 6}
# poke_df['GenerationLabel'] = poke_df['Generation'].map(gen_ord_map)
# 
# poke_df[['Name','Generation','Generationlabel']].iloc[4:10]
# 
# =============================================================================

vg_df = pd.read_csv('vgsales.csv', encoding='utf-8')

unique_genres = np.unique(vg_df[['Genre']])
print("Total game genres:", len(unique_genres))
print(unique_genres)

from sklearn.feature_extraction import FeatureHasher
fh = FeatureHasher(n_features=6, input_type='string')
hashed_features = fh.fit_transform(vg_df['Genre'])
hashed_features = hashed_features.toarray()