#!/usr/bin/env python3
import numpy as np
## ============================ ##
# This will create a population 
# with pop_size individuals and 
# in each individual, nr_binary_var
# bits is randomly generated.
## ============================ ##

'''
In: pop_size, nr_binary_var
Out: individual (pop_size, nr_binary_var)
'''

def individuals(pop_size, nr_binary_var):
	individual=np.zeros((pop_size, nr_binary_var))
	for ixd_pop in range(pop_size):
		for jxd_var in range(nr_binary_var):
			np.random.seed()
			individual[ixd_pop, jxd_var]=np.random.randint(0,pop_size*nr_binary_var)%2
	return individual

'''
# Verify individuals function
pop_size=6
nr_binary_var=10
individual=individuals(pop_size,nr_binary_var)
print(individual)
'''
