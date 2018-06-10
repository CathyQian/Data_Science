# -*- coding: utf-8 -*-
"""
Below is Python code of Naive Bayes Algorithm from scratch.
Input: data
Output: predicted class values and prediction accuracy

Reference: https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
Note: 1, The original code in the above link have one big bug: it doesn't calculate P(y). 
This bug is fixed her by adding the probY function.
2, dict.iteritems changed into dict.items in Python 3.5
3, The right way to access the ith row of a pandas dataframe is df[i:i+1], not df[i]
4, Input data is pandas dataframe
"""

"""
===============================================================================
1, Separate data by class
===============================================================================
"""
def separateByClass(data):
    """input the training dataset, output a dictionary contains class value (key)
    and each entry with this class value (value)
    """
    
    separated = {}
    for i in range(len(data)):
        vector = np.array(data[i:i+1])
        temp = vector[-1]
        # assume the last column of data is the class value
        if temp[-1] not in separated:
            separated[temp[-1]] = []
        tempp = temp[0:len(temp) - 1]
        separated[temp[-1]].append(tempp)
    return separated

"""
===============================================================================
2, Calculate Mean and standard deviation of each attribute for each class value.
===============================================================================
"""
import math
def meanValue(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    """ sigma = sqrt(sum(x-u)2/(n-1))
    """
    avg = meanValue(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers) - 1)
    
    return math.sqrt(variance)

def summarize(data):
    """ input data with the same class value
        calculate the mean and the standard deviation for each attribute
    """
    summaries = [(meanValue(attribute), stdev(attribute)) for attribute in zip(*data)]
    
    return summaries

def summarizeByClass(data):
    """ input train data, output list summaries with index as class value and 
    mean and standard deviation of each attribute as content
    """
    separated = separateByClass(data)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries


"""
===============================================================================
3, Make predictions: calculate posterior P of each class and use the class value
 with max P as prediction.
===============================================================================
"""
def calculateProbability(x, mean, stdev):
    """return Gaussian probability P(x/y) given x, mean and stdev of y
    """
    exponent = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev, 2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent

def probY(data):
    """calculate P(y) and return a dictionary {classValue: P(y)}
    """
    pY = {}
    n = len(data)
    separated = separateByClass(data)
    for classValue, instances in separated.items():
          pY[classValue] = len(instances)/float(n)
    return pY
    
    
def calculateClassProbabilities(summaries, inputVector, pY):
    """calculate the Gaussian probability for inputVector and return sumP(x[i]/y)
    in a dictionary
    """
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = pY[classValue]
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities

def predict(summaries, inputVector, pY):
    """ find the max p in the P(x[i]/y) dictionary and return corresponding class
    labels as predicted class label.
    """
    probabilities = calculateClassProbabilities(summaries, inputVector, pY)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel
        
def getPredictions(summaries, testSet, pY):
    """ input the whole testset and return all the predicte class value in a list
    """
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i:i+1], pY)
        predictions.append(result)
    return predictions


"""
===============================================================================
4, Get Accuracy: compare the predicted class values in the test dataset and 
calculate the prediction accuracy
===============================================================================
"""
def getAccuracy(testSet, predictions):
    correct = 0
    n = len(testSet.columns)
    for x in range(len(testSet)):
        if testSet[n-1][x] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))



"""
===============================================================================
Main function
===============================================================================
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# read in x, y as numpy array
df = pd.read_csv('data.csv')
n = len(df.columns)
y = df.iloc[:, n-1:n]
X = df.iloc[:, 0:n-1]
x = X.values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 2018)

train = pd.DataFrame(np.concatenate((x_train, y_train), axis = 1))
test = pd.DataFrame(np.concatenate((x_test, y_test), axis = 1))

# prepare model
summaries = summarizeByClass(train)

# test model
pY = probY(train)
predictions = getPredictions(summaries, test, pY)

accuracy = getAccuracy(test, predictions)
print("Accuracy:", accuracy)
