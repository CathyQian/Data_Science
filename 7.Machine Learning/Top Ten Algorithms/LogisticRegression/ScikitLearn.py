# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

'''
====================================================================================================
scikit-learn
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

Input: data file
Output: coefficient, intercerpt, fitted y on any input data, accuracy, number of iterations
    
====================================================================================================
'''
import pandas as pd
from sklearn.linear_model import LogisticRegression

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
          tol: convergence condition (or tolerance for stopping criteria)
          fit_intercept: specifies whether intercept is needed or not
          random_state:seed used by the random number generator
          max_iter: maximum number of iterations
'''
clf = LogisticRegression(tol = 1e-8, fit_intercept = True, random_state = 5, max_iter = 100)

# Fitting the input (x, y)
clf.fit(x, y)

# Get predicted y value
yfit = clf.predict(x)
accuracy = clf.score(x, y)
print(accuracy)

# output parameters: coefficients, intercept, number of iterations
coeff = clf.coef_
intercept = clf.intercept_
n_iter = clf.n_iter_
print(coeff, intercept, n_iter)
