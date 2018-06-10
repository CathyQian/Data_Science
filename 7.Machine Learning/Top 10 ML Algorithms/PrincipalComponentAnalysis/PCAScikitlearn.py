# -*- coding: utf-8 -*-
'''
==================================================================================
scikit-learn
Link:http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
    
Input: x
Output: new x with reduced dimension, percentage of variance explained by each selected components,
average log-likelihood of all samples
==================================================================================
'''
import pandas as pd
from sklearn.decomposition import PCA

# read in x, y as numpy array
df = pd.read_csv('data.csv', names = ["A", "B", "C", "D", "E", "F", "G", "H"])
df = df.drop(["H"], axis = 1)
x = df.values

# define model
''' set model parameters:
         n_components: number of components to keep
         random_state: seed used by the random number generator
'''
clf = PCA(n_components = 3, random_state = 2018)

# Fit the input x and return the new X with reduced dimension
clf.fit_transform(x)

# output parameters: 
components = clf.components_  # principal axes in feature space
variance = clf.explained_variance_ratio_ # percentage of variance explained by each of the selected components
print(components, variance)

# return the average log-likelihood of all samples
accuracy = clf.score(x)
print(accuracy)