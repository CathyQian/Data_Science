# -*- coding: utf-8 -*-

'''
==================================================================================
scikit-learn
Link:http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    
Input: data file
Output: predicted y value, support vectors, prediction accuracy

Notes: sklearn.svm.svc and set kernel = 'linear' is different from sklearn.svm.LinearSVC
mathematically. Thus they get different accuracy for the same problem. 
==================================================================================
'''
import pandas as pd
from sklearn.svm import SVC

# read in x, y as numpy array
df = pd.read_csv('data.csv', names = ["A", "B", "C", "D", "E", "F", "G", "H"])
y = df["H"]
df = df.drop(["H"], axis = 1)
x = df.values

# define model
''' set model parameters:
          C: penalty parameter C of the error term
          kernel: specifies the kernel type to be used in the algorithm
          random_state: seed of the pseudo random number generator to use when shuffling the data 
'''
clf = SVC(C = 1.0, kernel = 'rbf', random_state = 2018  )

# Fitting the input (x, y)
clf.fit(x, y)

# Get predicted y value
yfit = clf.predict(x)

# output parameters: probability of each class, number of training samples observed in each class
support_vectors = clf.support_vectors_  # support vectors
print(support_vectors)

# return the mean accuracy on the given test data and labels
accuracy = clf.score(x, y)
print(accuracy)