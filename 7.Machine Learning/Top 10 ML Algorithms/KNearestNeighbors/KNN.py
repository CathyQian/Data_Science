# -*- coding: utf-8 -*-
'''
===============================================================================
Below is the Python implementation of the K nearest neighbors classification algorithm

Input: training data, y label, K value, new sample
Output: label of new sample
===============================================================================
'''
import numpy as np
from collections import Counter

def p2pdist(a, b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i]-b[i])*(a[i]-b[i])
    return np.sqrt(distance)

def knn(x, y, K, new_sample):
    '''
    x is numpy array and y is list
    Return the predicted y label for one single new_sample
    '''
        
    # calculate the Eulidean distance between the new sample and all training samples
    d = []

    for i in range(len(x)):
        z = p2pdist(x[i], new_sample)
        d.append([z, i, y[i]])
    distances = np.array(d)

    # select the K smallest values from distances
    kmin = []
    np.sort(distances, axis = 0)
    kmin = distances[:K]
    
    # store corresponding y labels in yvalue list
    yvalue = []
    for j in range(K):
        yvalue.append(kmin[j][2])
        
    counter = Counter(yvalue) # returns a dictionary
    max_count = max(counter.values())
    mode = [k for k,v in counter.items() if v == max_count] 
    
    return mode

def knnfortest(x, y, K, x_test):
    predicted_y = []
    for new_sample in x_test:
        ytest = knn(x, y, K, new_sample)
        predicted_y.append(ytest)
    return predicted_y

'''
===============================================================================
'''
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data.csv')
df = df.dropna(axis = 0, how = 'any')
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df['Embarkloc'] = df['Embarked'].map({'C': 1, 'Q': 2, 'S': 3})

y = np.array(df['Survived'])

df = df.drop(['Survived', 'Sex', 'Embarked'], axis = 1)
x = df.values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 7)
K = 5
predicted_y = []
predicted_y = knnfortest(x_train, y_train, K, x_test)

# calculate accuracy
accuracy = len([i for i, j in zip(y_test, predicted_y) if i == j])/len(y_test)
print(accuracy)
