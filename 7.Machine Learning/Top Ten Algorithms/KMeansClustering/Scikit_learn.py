# -*- coding: utf-8 -*-

'''
==================================================================================
scikit-learn
Link: http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

Input: 
   1) X (numpy array): contains m elements
   2) K (integer): number of clusters

Output:
   1) C (numpy array): position of centroids
   2) idx (list of integer): index of centroid of each element in X
   3) all_J (list of float number): record of all cost function J during iteration 
==================================================================================
'''
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
f1 = data['x1'].values
f2 = data['x2'].values
X = np.array(list(zip(f1, f2)))
K = 3


''' set parameters:
    n_clusters: Number of clusters
    init: choose K random points from data for initial centroid
    max_iter: maximum number of iterations
    tol: convergence condition for cost function
    random_state: seed used by the random number generator, for reproducibility
'''
kmeans = KMeans(n_clusters = K, init = 'random', n_init = 1, max_iter = 10, tol = 1e-5, random_state = 7)

# Fitting the input data (or any other methods)
kmeans = kmeans.fit(X)

# Getting the cluster labels (or any other methods)
labels = kmeans.predict(X)

# Centroid values (or any other attributes)
C = kmeans.cluster_centers_
Xlabels = kmeans.labels_
J = kmeans.inertia_

plt.scatter(f1, f2, c = 'b', s = 6)
plt.scatter(C[:, 0], C[:, 1], c='r', s=100, marker='*')
plt.xlabel('x1')
plt.ylabel('x2')