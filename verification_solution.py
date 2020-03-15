#!/usr/bin/env python3
import numpy as np

## =========================================== ## 
# This software uses brute forces to find all
# possible solutions of unknown variable X, 
# where each dimension value of X is 0 or 1
## =========================================== ##

## =========================================== ##
# We will assume the cost function is defined:
# f(X)=x1*a1+x2*a2+...+xN*aN
# f(X)=X*A
# X is an individual with in the population
# X = [x1, x2, ..., xn] 
# A is known coefficient vector 
# A = [a1, a2, ..., an]
## ============================================ ##

# Assume that unknown variable X has 10 dimensions: X: (10, ) 
nr_binary_var=10
X=np.zeros((2**nr_binary_var,nr_binary_var))

# Assume that known vector A is defined as follows:
A=np.array([1.1, 1.7, -2.2, -1.6, 0.4, -3.1, 4.3, -0.1, -3.5, 2.4 ])

# Retrieve all possible solutions of unknown X
for idx in range(2**nr_binary_var):
	X_tmp='{0:010b}'.format(idx)
	X_tmp=np.array(list(map(int, X_tmp)))
	X[idx]=X_tmp

print('All possible solutions: \n', X)
obj_val=np.dot(X,A)
print('All the cost values: \n ', obj_val)
idx_min_obj=np.argmin(obj_val)
print('Global minimum value: \n', obj_val[idx_min_obj])
print('The vector X among all possible solutions that have minimum value is: \n', X[idx_min_obj])
