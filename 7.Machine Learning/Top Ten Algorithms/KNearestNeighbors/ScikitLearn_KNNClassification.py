# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

'''
Classification
====================================================================================================
scikit-learn
http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier

Input: training data, y label, K value, new sample
Output: label of new sample
====================================================================================================
'''
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# read in input data
df = pd.read_csv('data.csv')
df = df.dropna(axis = 0, how = 'any')
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df['Embarkloc'] = df['Embarked'].map({'C': 1, 'Q': 2, 'S': 3})

y = df['Survived']
df = df.drop(['Survived', 'Sex', 'Embarked'], axis = 1)
x = df.values

# define model
''' set model parameters:
          n_neighbors: number of neighbors to use
          p: p = 1 means measuring manhattan_distance, p = 2 means measuring euclidean distance
'''
KNN = KNeighborsClassifier(n_neighbors = 5, p =2)

# Fitting the input (x, y)
KNNeighbors = KNN.fit(x, y)

# Get predicted y value
yfit = KNNeighbors.predict(x)
accuracy = KNNeighbors.score(x, y)
print(accuracy)

