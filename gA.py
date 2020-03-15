#!/usr/bin/env python3
## ================================ ##
# Load libraries
## ================================ ##
import numpy as np

## ================================ ##
# Load prepared functions
## ================================ ##
from pOPULATION import individuals
from fITNESS import fitness
from sELECTION import selection
from cROSSOVER import crossover
from mUTATION import mutation
from eLITISM import elitism

## ================================= ##
# Genetic Algorithm (GA) Variables 
# population should be even number
## ================================= ##
pop_size=6 
nr_binary_var=10
prob_crossover=0.85
prob_mutation=0.01
max_iteration=50

## ================================ ##
# Main GA algorithms
## ================================ ##

# ******************* Step 1 **********************
# Initialization of population includingindividuals
# Compute fitness of all individuals in population
# Pick the minimum fitness
# *************************************************
# Iteration 0:
population=individuals(pop_size,nr_binary_var)
fitness_val=np.array([fitness(population[idx]) for idx in range(pop_size)])
idx_min_fitness=np.argmin(fitness_val)
print("iteration 0 ", ": cost value = ",fitness_val[idx_min_fitness])

# ******************* Step 2 ********************** 
# create new population by using many functions as: 
#   ---> selection 
#   ---> crossover 
#   ---> mutation
#   ---> elitism
# *************************************************
population_new=np.zeros((pop_size, nr_binary_var))

# Iteration from 1 onward
for idx_iter in range(1,max_iteration+1):
	for idx_pop in range(0,pop_size,2):

	# selection; 
	# two individuals from population 
	# using tournament selection
		idx_select1=selection(pop_size,population)
		parent1=population[idx_select1]
		idx_select2=selection(pop_size,population)
		parent2=population[idx_select2]

	# crossover;
	# from two selected individuals
	# cross partial genes each other
		child1, child2=crossover(parent1, parent2, nr_binary_var, prob_crossover)
	
	# mutation;
	# from child1, randomly flip some bits
	# from child2, randomly flop some bits
		child1=mutation(child1,nr_binary_var,prob_mutation)
		child2=mutation(child2,nr_binary_var,prob_mutation)
	 
	# assign to population_new
		population_new[idx_pop]=child1
		population_new[idx_pop+1]=child2
	
	# elitism
	# to keep the best in old population
	# and replace the worst in new population 
	# by the best in old
	population_tmp=elitism(population, population_new, pop_size)
	population=population_tmp.copy()
	
	# fitness for population
	fitness_val=np.array([fitness(population[idx]) for idx in range(pop_size)])
	idx_min_fitness=np.argmin(fitness_val)
	print("iteration ", idx_iter, ": cost value = ", fitness_val[idx_min_fitness])


