#!/usr/bin/env python3
import numpy as np

## =================================== ##
#  Input a child and then based on the 
#  rand() value compared to mutation 
#  probability, the bits will be changed
## =================================== ##

'''
Parameters: 
   In: child: (nr_binary_var, )
       nr_binary_var: scalar value
       prob_muatation: scalar value between (0,1) 
'''

def mutation(child,nr_binary_var,prob_mutation):
	for idx_var in range(nr_binary_var):
		np.random.seed()
		rand_tmp=np.random.rand()
		if rand_tmp<prob_mutation:
			child[idx_var]=1-child[idx_var]
	return child

'''
# Verify mutation
prob_mutation=0.05
nr_binary_var=10
child=np.array([0,1,1,1,1,0,0,0,0,1])
print('child before mutation: ', child)
child_mutation = mutation(child,nr_binary_var,prob_mutation)
print('child  after mutation: ', child_mutation)
'''
