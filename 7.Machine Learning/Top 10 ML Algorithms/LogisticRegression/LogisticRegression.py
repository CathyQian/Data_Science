# -*- coding: utf-8 -*-
'''
This is Python implementation of logistic regression algorithm.

===============================================================================
Input: data file

Output: theta(or weights), history of cost function J
===============================================================================
'''

import numpy as np

def logisticfunc(z):
    g = 1/(1 + np.exp(-z))
    return g    

def hvalue(x, theta):
    return logisticfunc(np.dot(x, theta.T))

def logisticRegression(x, y, alpha, iterations):
    # add x[0] = 1
    x = np.concatenate((np.array([[1]*x.shape[0]]).T, x), axis = 1)
    
    # initialize theta
    theta = np.zeros(x.shape[1])
    m = x.shape[0]
    
    hist_J = []
    
    # gradient descent
    for iteration in range(iterations):
        
        h = hvalue(x, theta)
        
        # Difference b/w Hypothesis and Actual Y
        loss = h - y
        
        # Gradient Calculation
        gradient = np.dot(x.T, loss) / m
        
        # update theta
        theta = theta - alpha * gradient
        
        # calculate cost function J
        J = 1/m*(-np.dot(y, np.log(h)) - np.dot((1 - y), np.log(1 - h)))
        
        # record history of J
        hist_J.append(J)
    
    return theta, hist_J


'''
===============================================================================
main function to apply logistic regression
note: the data comes from Titanic Kaggle competition with slight modification
===============================================================================
'''


import pandas as pd
import matplotlib.pyplot as plt

# read in input data
df = pd.read_csv('data.csv')
df = df.dropna(axis = 0, how = 'any')
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df['Embarkloc'] = df['Embarked'].map({'C': 1, 'Q': 2, 'S': 3})

y = df['Survived']
df = df.drop(['Survived', 'Sex', 'Embarked'], axis = 1)
x = df.values

alpha = 0.001
iterations = 30

hist_J = []
theta, hist_J = logisticRegression(x, y, alpha, iterations)

# plot hist_J
plt.plot(hist_J)
plt.xlabel('Iterations')
plt.ylabel('Cost function J')
print(theta)