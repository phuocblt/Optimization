#!/usr/bin/env python3
import numpy as np

## ===================================== ##
#  Take 2 individuals in the population 
#  and then interchange 2 parts from 2 
#  individuals to create 2 new individuals
## ===================================== ##

'''
Parameters:
   In: parent1 : (nr_binary_var, ) 
       parent2 : (nr_binary_var, )
	   nr_binary_var : scalar value is 0 or 1
       prob_crossover: scalar between (0, 1)
   Out: child1 : (nr_binary_var, )
        child2 : (nr_binary_var, ) 
'''
def crossover(parent1,parent2,nr_binary_var,prob_crossover):
	np.random.seed()
	point_xover=int(np.rint(np.random.rand()*nr_binary_var))

	first_part=parent1[0:point_xover]
	second_part=parent2[point_xover:]
	child1=np.concatenate([first_part,second_part])

	first_part=parent2[0:point_xover]
	second_part=parent1[point_xover:]
	child2=np.concatenate([first_part,second_part])

	if np.random.rand()>prob_crossover:
		child1=parent1
	if np.random.rand()>prob_crossover:
		child2=parent2	
	return child1, child2

'''
# Verify function crossover
prob_crossover=0.85
nr_binary_var=10
parent1=np.array(np.arange(0,nr_binary_var))
parent2=np.array(np.arange(10,2*nr_binary_var))
print('Two parents are:\n ', parent1,'\n',parent2)
child1, child2 = crossover(parent1,parent2,nr_binary_var,prob_crossover)
print('Two new child are:\n ', child1,'\n', child2)
'''
