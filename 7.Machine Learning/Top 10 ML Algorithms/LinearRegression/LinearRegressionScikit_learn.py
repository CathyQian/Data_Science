# -*- coding: utf-8 -*-

'''
==================================================================================
scikit-learn
Link: http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

Input: data file
Output: coefficient, intercerpt, fitted y
    
==================================================================================
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

# read in x, y as numpy array
data = pd.read_csv('Housing.csv')
x = data['lotsize'].values
y = data['price'].values

# define model
''' set model parameters:
          fit_intercept: calculate intercept for this model or not
          normalize: whether to normalize X before regression or not
          copy_X: if True, X will be copied; else, it may be overwritten
'''
LR = LinearRegression(fit_intercept = True, normalize = False, copy_X = True)

# Fitting the input (x, y)
LRegression = LR.fit(x[:, np.newaxis], y)

# Get predicted y value
yfit = LRegression.predict(x[:, np.newaxis])

# output parameters: coefficients and intercept
coeff = LRegression.coef_
intercept = LRegression.intercept_

plt.scatter(x, y, c = 'b', s = 6)
plt.plot(x, yfit, 'r')
plt.xlabel('lot size')
plt.ylabel('price')