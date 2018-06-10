# -*- coding: utf-8 -*-

'''
===============================================================================
Below is the pseudo code for logistic regression

Input: data file
Output: coefficient, intercerpt, history of cost function J

===========================================================================
'''
1, define logistic function g(z) = 1/(1+exp(-z))
2, define cost function J
   J = 0
   for i in range(m):
       j += 1/m*(-y[i]*log(h(x[i]))-(1-y[i])*log(1-h(x[i])))
3, gradient descent
    repeat until convergence:
    for j in range(len(theta)):
        for i in range(m):
            thetaj := thetaj - alpha*/m*(h(x[i])-y[i])*x[i]
    



