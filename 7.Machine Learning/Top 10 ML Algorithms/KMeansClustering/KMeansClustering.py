# -*- coding: utf-8 -*-

'''
===============================================================================
This is Python implementation of K-means clustering algorithm.

Input: 
   1) X (numpy array): contains m elements
   2) K (integer): number of clusters

Output:
   1) C (numpy array): position of centroids
   2) idx (list of integer): index of centroid of each element in X
   3) all_J (list of float number): record of all cost function J during iteration 
===============================================================================
'''


import numpy as np
from matplotlib import pyplot as plt

def kMeans(X, K):
    
    # Initialize K centroids that are to be used in K-means on the dataset X with random values between X.max and X.min.
    Cx = np.random.random_sample(K)*(np.max(X)- np.min(X)) + np.min(X)
    Cy = np.random.random_sample(K)*(np.max(X)- np.min(X)) + np.min(X)
    C = np.array(list(zip(Cx, Cy)), dtype=np.float32)
    
    # make scatter plot of the data
    plt.figure()
    plt.scatter(f1, f2, c = 'b', s = 6)
    plt.xlabel('x1')
    plt.ylabel('x2')
    
    # set convergence condition and repeat iteration until it is satisfied.    
    # set convergence condition
    epsilon = 1e-5
    
    # initialize cost function and difference
    J_old, delta = float('inf'), 1.0
    m = len(X)
    all_J = []
    
    # repeat the following loop until convergence condition is satisfied
    iii = 0
    while delta > epsilon:
        iii += 1
        
        # label each element in X with its nearest centroid index from 1 to K
        # initialize index values
        idx = np.zeros(m)
        for i in range(m):
            dist = np.linalg.norm(X[i] - C, axis = 1)
            idx[i] = np.argmin(dist)
                
        # update the position of the K centroids
        for i in range(K):
            points = [X[j] for j in range(m) if idx[j] == i]
            C[i] = np.mean(points, axis = 0)
        
        
        # calculate cost function
        J_new = 0
        for i in range(m):
            J_new += 1/m * (np.linalg.norm(X[i]-C[int(idx[i])], axis = 0))**2
            
        delta = J_old - J_new 
        J_old = J_new
        all_J.append(J_new)
        
        # plot the data with centroids
        plt.figure( iii )
        plt.scatter(f1, f2, c = 'b', s = 6)
        plt.scatter(C[:, 0], C[:, 1], c='r', s=100, marker='*')
        plt.xlabel('x1')
        plt.ylabel('x2')
       
    return C, idx, all_J

'''
===============================================================================
main function to use K-Means clustering algorithm.
===============================================================================
'''

import pandas as pd

data = pd.read_csv('data.csv')
f1 = data['x1'].values
f2 = data['x2'].values
X = np.array(list(zip(f1, f2)))
K = 3
kMeans(X, K)


    
    