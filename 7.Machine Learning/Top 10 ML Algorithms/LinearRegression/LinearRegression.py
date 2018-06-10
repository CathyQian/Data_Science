# -*- coding: utf-8 -*-

'''
This is Python implementation of linear regression algorithm.
'''

'''
===============================================================================
Univariant LR
Input: (x, y) pairs
Output: coefficient theta[1]], intercerpt theta[0], fitted y, cost function history J_hist
===============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt

def univariantLinearR(X, Y, alpha, iterations):
    J_hist = [0] * iterations
    fittedY = [0] * len(X)
    m = len(X)
    
    # initialize two theta values
    theta0 = np.random.random_sample()
    theta1 = np.random.random_sample()
    
    # gradient descent
    for iteration in range(iterations):
        temp0, temp1 = theta0, theta1
        J = 0
        for i in range(m):
            J += 1/(2*m)*(temp0 + temp1*X[i]-Y[i])**2
            theta0 -= alpha/m*(temp0 + temp1*X[i] - Y[i])
            theta1 -= alpha/m*(temp0 + temp1*X[i] - Y[i])*X[i]
                  
        J_hist[iteration] = J
        
    # calculate fitted Y value    
    fittedY = theta0 + np.dot(theta1, X)
    return [theta0, theta1], J_hist, fittedY

'''
===============================================================================
main function to use univariant linear regression algorithm.
===============================================================================
'''

import pandas as pd

data = pd.read_csv('Housing.csv')
X = data['lotsize'].values
Y = data['price'].values
alpha = 1e-10
iterations = 1000
theta = [0]*2
J_hist, fittedY = [0]*iterations, [0]*len(X)
theta, J_hist, fittedY = univariantLinearR(X, Y, alpha, iterations)

# plot linear fitting line
plt.figure(1)
plt.scatter(X, Y, c='b')
plt.plot(X, fittedY, c='r')
plt.xlabel('lot size')
plt.ylabel('Price')

# plot cost function J versus number of iterations
plt.figure(2)
plt.plot(J_hist)
plt.xlabel('Iteration number')
plt.ylabel('Cost function J')

'''
===============================================================================
Multivariant Linear Regression
Input: (X, Y) pairs, intial theta
Output: coefficient theta, fitted y, cost function history J_hist
===============================================================================
'''
def multivariantLinearR(X, Y, theta, alpha, iterations):
    
    cost_history = [0] * iterations
    m = len(Y)
    
    # gradient descent
    for iteration in range(iterations):
        # Hypothesis Values
        h = X.dot(theta)
        
        # Difference b/w Hypothesis and Actual Y
        loss = h - Y
        
        # Gradient Calculation
        gradient = X.T.dot(loss) / m
        
        # Changing Values of B using Gradient
        theta = theta - alpha * gradient
        
        # New Cost Value
        cost = np.dot(X.dot(theta)-Y, X.dot(theta)-Y)/(2*m)
        cost_history[iteration] = cost
        
    return theta, cost_history
