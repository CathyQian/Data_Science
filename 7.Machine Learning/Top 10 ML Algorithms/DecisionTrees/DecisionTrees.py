# -*- coding: utf-8 -*-
'''
This is Python implementation of decision tree classification algorithm.
The code is adapted from machinelearningmastry with modifications:
https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/
===============================================================================
Input: data file
Output: feature importance, predicted y value, prediction accuracy
===============================================================================
'''
# CART on the Bank Note dataset
from random import seed
from random import randrange
from csv import reader

# Load a CSV file
def load_csv(filename):
	file = open(filename, "rb")
	lines = reader(file)
	dataset = list(lines)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    '''
        index: index of features, this feature is the attribute
        value: attribute value used for splitting 
               < value, put into left child
               > value, put into right child
        dataset: input dataset
        
        return left and right child as lists
    '''
    
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    '''
       - assume one node is split into several groups and each group data is 
       stored in a list
       - all these data are categorized into classes stored in the classes list
       - output Gini index for a split dataset
    '''
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	gini = 0.0
	for group in groups:
		size = float(len(group))
		# avoid divide by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		# weight the group score by its relative size
		gini += (1.0 - score) * (size / n_instances)
	return gini

# Select the best split point for a dataset
def get_split(dataset):
    '''
    - calculate gini index of all possible splits with all features/values
    - return the split with minimum Gini cost
    '''
    # get all class values
	class_values = list(set(row[-1] for row in dataset))
	b_index, b_value, b_score, b_groups = 999, 999, 999, None
    # loop over all attributes/features and attribute values/rows
	for index in range(len(dataset[0])-1):
		for row in dataset:
          # split based on attribute and attribute values, get Gini index
          # for each split
			groups = test_split(index, row[index], dataset)
			gini = gini_index(groups, class_values)
          # find the minimum Gini index among all splits
			if gini < b_score:
				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
	return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Create a terminal node value
def to_terminal(group):
    '''
    the terminal group output the class with maximum counts
    '''
	outcomes = [row[-1] for row in group]
	return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
    '''
        - split stops when max_depth or min_size is met
        - remember the depth of each node
        - recursively split child node
        - each node contains: index, value, groups(contains left and right);
          here index and value are the split condition
        
    '''
	left, right = node['groups']
	del(node['groups'])
	
    # check for a no split
   # if left or right is empty, stop splitting and create a terminal node with left + right
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		return
	
    # if maximum depth is already met, stop splitting and create left and right terminal nodes
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
    
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = get_split(left)
		split(node['left'], max_depth, min_size, depth+1)
	
    # process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = get_split(right)
		split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
        
    # start from splitting root, the first split is always guaranteed
    # so split separately instead of bringing into the split recursive loop
	 root = get_split(train)
	# then recursively split the rest of the node
    split(root, max_depth, min_size, 1)
	return root

# Make a prediction with a decision tree
def predict(node, row):
    # recursively predict a SINGLE row with all attributes (node values)
    # return class values of the row    
    # if row value < node attribute (or node value), go to left child
	if row[node['index']] < node['value']:
       # if left child is not empty, recursively loop child
		if isinstance(node['left'], dict): # if node['left'] or node['right'] is a dictionary
			return predict(node['left'], row)
       # if left child is empty, means it is terminal node, return node value 
       # (or class value) as prediction result
		else:
			return node['left']
   # do the same thing if split to the right child
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']

# Classification and Regression Tree Algorithm
def decision_tree(train, test, max_depth, min_size):
    # build a decision tree and predict results
    
	tree = build_tree(train, max_depth, min_size)
	predictions = list()
    
    # loop over all row
	for row in test:
		prediction = predict(tree, row)
		predictions.append(prediction)
	return(predictions)

'''
===============================================================================
Test CART on Bank Note dataset
===============================================================================
'''
seed(1)
# load and prepare data
filename = 'data_banknote_authentication.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
# evaluate algorithm
n_folds = 5
max_depth = 5
min_size = 10
scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))