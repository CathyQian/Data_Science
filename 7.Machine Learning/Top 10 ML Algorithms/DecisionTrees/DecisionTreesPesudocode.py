# -*- coding: utf-8 -*-

'''
===============================================================================
Below is the pseudo code for decision trees classification algorithm
Input: data file
Output: coefficient, intercerpt, feature importance

steps:
1, Split a dataset based on an attribute and an attribute value
2, Calculate the Gini index for a split dataset
3, Select the best split point for a dataset
4, Create a terminal node value
5, Create child splits for a node or make terminal
6, Build a decision tree
7, Make a prediction with a decision tree
===========================================================================
'''
'''
1, Split a dataset based on an attribute and an attribute value
'''

    def test_split(index, value, dataset):
        '''
        index: index of features, this feature is the attribute
        value: attribute value used for splitting 
               < value, put into left child
               > value, put into right child
        dataset: input dataset
        
        return left and right child as lists
        '''
        for row in dataset:
            if row[index] < value:
			      left.append(row)
		     else:
			      right.append(row)
	 reture left, right

'''
2, Calculate the Gini index for a split dataset
'''

    def gini_index(groups, classes):
        '''
        - assume one node is split into several groups and each group data is 
        stored in a list
        - all these data are categorized into classes stored in the classes list
        - output Gini index for a split dataset
        '''
	    for group in groups:
		    # score the group based on the score for each class
		    for class_val in classes:
			    p = number of values with class_val in this group/number of values with class_val in all groups
			    score = p * p
		    # weight the group score by its relative size
		    gini += (1.0 - score) * ( group size / sum of all group sizes)
	    return gini

'''
3, Select the best split point for a dataset
'''   
    def get_split(dataset):
        '''
        - calculate gini index of all possible splits with all features/values
        - return the split with minimum Gini cost
        '''
	    # loop over all attributes/features and attribute values/rows
        for index in range(len(dataset[0])-1):
		     for row in dataset:
               # split based on attribute and attribute values, get Gini index
               # for each split
			    groups = test_split(index, row[index], dataset)
			    gini = gini_index(groups, class_values)
               # find the minimum Gini index among all splits
			    gini = min(all gini)		    
	    return {'index':b_index, 'value':b_value, 'groups':b_groups}

'''
4, Create a terminal node value
'''
    def to_terminal(group):
        '''
        the terminal group output the class with maximum counts
        '''
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)

'''
5, Create child splits for a node or make terminal
'''
    def split(node, max_depth, min_size, depth):
        '''
        - split stops when max_depth or min_size is met
        - remember the depth of each node
        - recursively split child node
        - each node contains: index, value, groups(contains left and right);
          here index and value are the split condition
        
        '''
        left, right = node['groups']
      
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

'''
6, Build a decision tree
'''
    def build_tree(train, max_depth, min_size):
        
        # start from splitting root, the first split is always guaranteed
        # so split separately instead of bringing into the split recursive loop
	    root = get_split(train)
	    # then recursively split the rest of the node
        split(root, max_depth, min_size, 1)
	    return root
    
'''    
7, Make a prediction with a decision tree
'''
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
