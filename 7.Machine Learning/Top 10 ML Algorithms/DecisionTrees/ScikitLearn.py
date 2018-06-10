# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

'''
====================================================================================================
scikit-learn
Link: http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier

Input: data file
Output: c
    
====================================================================================================
'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

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
          criterion: gini impurity as splitting requirement
          max_depth: maximum depth of a tree
          min_samples_split: minimum sample of node to stop splitting
          max_features: the number of features to consider when looking for the best split
          random_state: seed used by the random number generator
'''
DT = DecisionTreeClassifier(criterion = 'gini', max_depth = 4, min_samples_split = 2, max_features=4, 
                            random_state = 9)
# Fitting the input (x, y)
DTree = DT.fit(x, y)

# Get predicted y value
yfit = DT.predict(x)

# return the mean accuracy on the given test data and labels
accuracy = DT.score(x, y)
print(accuracy)

''' output parameters: coefficients, intercept, number of iterations
'''
# importance of features, the higher, the more important the feature (Gini importance)
feature_importance = DTree.feature_importances_

print(feature_importance)