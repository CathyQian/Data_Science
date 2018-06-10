# -*- coding: utf-8 -*-

"""
===============================================================================
Below is the pseudo code for Naive Bayes classification algorithm
Input: data file
Output: probability of each class, prediction accuracy

=========================================================================
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
    return pY
    
    
def calculateClassProbabilities(summaries, inputVector, pY):
    """calculate the Gaussian probability for inputVector and return sumP(x[i]/y)
    in a dictionary
    """
    return probabilities

def predict(summaries, inputVector, pY):
    """ find the max p in the P(x[i]/y) dictionary and return corresponding class
    labels as predicted class label.
    """
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

