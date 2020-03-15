#!/usr/bin/env python3
import numpy as np
from fITNESS import fitness
## ============================================= ##
#  Tournament selection will be used as follows:
#   1) choose best individual:
#		+ Randomly select 3 (or N) individuals from 
#		  popupation
#   	+ Then choose the best fitness among 3 (or N).
## ============================================= ##
'''
Parameters:
   In: pop_size: scalar value
       population: (pop_size, nr_binary_var)
   Out: index_min : scalar number (where the minimum fitness is found among 3 randomly chosen individual)
'''

def selection(pop_size, population):
	fitness_tmp=np.zeros(3)
	idx_range=np.arange(pop_size)

	# randomly choose individual in population and compute fitness
	np.random.shuffle(idx_range)
	idx_rand0=idx_range[0]
	fitness_tmp[0]=fitness(population[idx_rand0])
    
	# randomly choose individual in population and compute fitness 
	np.random.shuffle(idx_range)
	idx_rand1=idx_range[0]
	fitness_tmp[1]=fitness(population[idx_rand1])

	# randomly choose individual in population and compute fitness
	np.random.shuffle(idx_range)
	idx_rand2=idx_range[0]
	fitness_tmp[2]=fitness(population[idx_rand2])

	# compute the index where the fitness is minimum among 3 random individual
	index_min=np.argmin(fitness_tmp)
	
	return index_min

'''
# Verify selection function
pop_size=6
nr_binary_var=10
population=np.array([np.random.randint(0,pop_size*nr_binary_var)%2 for i in range(pop_size*nr_binary_var)]).reshape(pop_size,nr_binary_var)
print('Population: \n ', population)
index_min = selection(pop_size, population)
print('Index minimum: \n', index_min)
'''
