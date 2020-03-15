#!/usr/bin/env python3
import numpy as np
from fITNESS import fitness
## ===================================================== ##
#  Given new population  and old population, 
#  compare the best old fitness and the best new fitness, 
#  if the best old fitness is less the best new fitness, 
#  then keep the best individual old by replacing the worst 
#  new individual by the best old individual.
## ===================================================== ##
'''
Parameters:
   In: pop_old: (pop_size, nr_binary_var)
       pop_new: (pop_size, nr_binary_var)
       pop_size: Scalar value
   Out: pop_tmp: (pop_size, nr_binary_var)
'''

def elitism(pop_old, pop_new, pop_size):
	pop_tmp=pop_new.copy()
	fitness_old=np.array([fitness(pop_old[i]) for i in range(pop_size)])
	fitness_new=np.array([fitness(pop_new[i]) for i in range(pop_size)])
	
	idx_min_old=np.argmin(fitness_old)
	idx_min_new=np.argmin(fitness_new)
	idx_max_new=np.argmax(fitness_new)

	# if the best old fitness better the best new fitness
	# replace the worst new individual by the best old individual
	if fitness_old[idx_min_old]<fitness_new[idx_min_new]:
		pop_tmp[idx_max_new]=pop_old[idx_min_old]
	return pop_tmp

'''
# Verify elitism function:
pop_size=6
population_new=np.ones((pop_size,10))
population_old=np.array([np.random.randint(60)%2 for i in range(60)]).reshape(6,10)
print('Old population: \n', population_old) 
print('New population: \n' , population_new)

population_elitism=elitism(population_old, population_new, pop_size)
print('Population after comparing: \n', population_elitism)
'''
