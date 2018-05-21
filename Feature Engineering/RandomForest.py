import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sn 
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

# save load_iris() sklearn dataset to iris
# if you'd like to check dataset type use: type(load_iris())
# if you'd like to view list of attributes use: dir(load_iris())
iris = load_iris()

# np.c_ is the numpy concatenate function
# which is used to concat iris['data'] and iris['target'] arrays 
# for pandas column argument: concat iris['feature_names'] list
# and string list (in this case one string); you can make this anything you'd like..  
# the original dataset would probably call this ['Species']
data_iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

# =============================================================================
# 
# sn.pairplot(data = data_iris)
# =============================================================================

feature_cols = iris['feature_names'] 
target_cols = iris['target']
X= data_iris[feature_cols]
Y = data_iris['target']

X_Train,X_Test ,y_Train,y_Test = train_test_split(X,Y,test_size = .25)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators = 25)
classifier.fit(X_Train,y_Train)

predict = classifier.predict(X_Test)

conf = confusion_matrix(y_Test , predict)

