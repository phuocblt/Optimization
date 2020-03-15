#!/usr/bin/env python3
import numpy as np

## ==================================== ##
# We will minimize the cost for function
# f(X)=x1*a1+x2*a2+...+xN*aN
# f(X)=X*A
# X is an individual with in the population
# X = [x1, x2, ..., xn] 
# A is known coefficient vector 
# A = [a1, a2, ..., an]
## ==================================== ##
'''
Parameters:
   In: X: (nr_binary_var, )
   Out: fitness: scalar value
'''
def fitness(X):
	A = np.array([1.1, 1.7, -2.2, -1.6, 0.4, -3.1, 4.3, -0.1, -3.5, 2.4 ])
	cost = np.dot(A,X)
	return cost

'''
# Verify fitness function
nr_binary_var=10
X= np.array([1 for _ in range(nr_binary_var)])
print(fitness(X))
'''
