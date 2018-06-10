# -*- coding: utf-8 -*-

'''
==================================================================================
scikit-learn
Link: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

Input: data file
Output: accuracy, feature importance, fitted y
    
==================================================================================
'''
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# read in x, y as numpy array
df = pd.read_csv('data.csv')
df = df.dropna(axis = 0, how = 'any')
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df['Embarkloc'] = df['Embarked'].map({'C': 1, 'Q': 2, 'S': 3})

y = df['Survived']
df = df.drop(['Survived', 'Sex', 'Embarked'], axis = 1)
x = df.values

# define model
''' set model parameters:
          n_estimators: the number of trees in the forest
         // The following parameters are the same as those in decision trees.
          criterion: the function to measure the quality of a split
          max_features: the number of features to consider when looking for the best split
          max_depth: the maximum depth of the tree
          random_state: the seed used by the random number generator
'''
clf = RandomForestClassifier(n_estimators = 3, criterion = 'gini', max_depth = 4, min_samples_split = 2, max_features=4, 
                            random_state = 9 )

# Fitting the input (x, y)
clf.fit(x, y)

# Get predicted y value
yfit = clf.predict(x)

# output parameters: coefficients and intercept
coeff = clf.feature_importances_

# return the mean accuracy on the given test data and labels
accuracy = clf.score(x, y)
print(accuracy)
print(coeff)