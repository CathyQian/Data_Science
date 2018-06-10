# -*- coding: utf-8 -*-
'''
===============================================================================
Below is the pseudo code for K nearest neighbors classification algorithm

Input: training data,y label, K value, new sample
Output: label of new sample
===========================================================================
'''
1, store the training samples in an array
# assume train is the imported dataframe containing all the training samples.
    train = train.values
2, calculate the Eulidean distance between the new sample and all training samples

def p2pdist(a, b):
    distance = 0
    for i in range(len(i)):
        distance += (a[i]-b[i])*(a[i]-b[i])
    return np.sqrt(distance)

def dist(train, new_sample):
    d = []
    for i in range(len(train)):
        z = p2pdist(train[i], new_sample)
        d.append([z, i])
    distances = np.array(d)
    return distances
3, select the K smallest values from the results of 2

def kmin(K, distances):
    np.sort(distances, axis = 0)
    return distances[:K]

4, find the mode labels of results from 3, return as result   

from collections import Counter
def modey(yvalues):
    counter = Counter(yvalues) # returns a dictionary
    max_count = max(counter.values())
    mode = [k for k,v in counter.items() if v == max_count] 
    return mode
