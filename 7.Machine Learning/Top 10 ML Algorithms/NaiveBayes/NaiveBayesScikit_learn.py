# -*- coding: utf-8 -*-

'''
==================================================================================
scikit-learn
Link:http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB
    
Input: data file
Output: probability of each class, prediction accuracy
==================================================================================
'''
import pandas as pd
from sklearn.naive_bayes import GaussianNB

# read in x, y as numpy array
df = pd.read_csv('data.csv', names = ["A", "B", "C", "D", "E", "F", "G", "H"])
y = df["H"]
df = df.drop(["H"], axis = 1)
x = df.values

# define model
''' set model parameters:
          priors: prior probabilities of the classes P(y), unknown here
'''
clf = GaussianNB(priors = None )

# Fitting the input (x, y)
clf.fit(x, y)

# Get predicted y value
yfit = clf.predict(x)

# output parameters: probability of each class, number of training samples observed in each class
class_prior = clf.class_prior_
class_count = clf.class_count_
print(class_prior, class_count)

# return the mean accuracy on the given test data and labels
accuracy = clf.score(x, y)
print(accuracy)