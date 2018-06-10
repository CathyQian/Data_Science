# -*- coding: utf-8 -*-
"""
===============================================================================
Below is the pseudo code for linear regression (univariant)

Input: (x, y) pairs
Output: coefficient, intercerpt, fitted y

===============================================================================
"""
1.start with some theta0, theta1
2.repeat until converge:
    theta0 := theta0 - alpha*1/m*(sum(h(x)-y) over m (x, y) pairs)
    theta1 := theta1 - alpha*1/m*(sum(h(x)-y) over m (x, y) pairs)*x
3,return theta0, theta1 and fitted y = theta0 + theta1*x