# -*- coding: utf-8 -*-
"""
===============================================================================
Below is the pseudo code for the K-means algorithm
Input: 
   1) X (numpy array): contains m elements
   2) K (integer): number of clusters

Output:
   1) C (numpy array): position of centroids
   2) idx (list of integer): index of centroid of each element in X
   3) all_J (list of float number): record of all cost function J during iteration  
===============================================================================
"""

Step 1. Randomly initialize K cluster centroids C
Step 2. Repeat until convergence:
    # Convergence condition: the difference between cost function J from two consecutive loops is smaller than a threshold.
    
    # label each element in X with its nearest centroid index j, j from 1 to K
    for i in range(m):
        idx := index of cluster centroids closest to X[i], range from 1 to K
    
    # update the position of the K centroids
    for k in range(1, K):
        C[k]: = average(mean) of points in X labeled with centroid k
        
    # calculate cost function
    J = 0
    for i in range(m):
       J += 1/m * (Euclidean distance between X[i] and the centroid it is 
                   labeled with)**2
        