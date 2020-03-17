# Genetic Algorithm
# 1. Introduction
Genetic algorithm (GA) is a heuristic search that is based on the idea of natural evolution in order to give the solution to some very complicated problems in reality ranging from Engineering, Economics, and so on. The main part of GA is a process of natural selection where some of individuals in the population are selected for producing their children in next generation. 

In general, the GA is deployed when we do not know how the solution looks like. For example, if we want to build a house with some predefined goals such as minimum cost for building, usage of cheap material but still good quality, as much rooms as possible, and so on. Fortnately, the GA will let us know the the best possible house that one will have after going through tremendously all possible aspects of demands but with relatively acceptable time.

# 2. Natural Selection
Natural environment is witnessing a rule in which eventually the strongest one will survive while the weak one will be eliminated. The GA is based on the natural selection uses the same theory to remove the weak ones (e. g., characters, traits, genes, ...) while keep the best solution. 

The GA is strongly inspired by the natural selection that are depicted in the following figures. The figure is a closed-loop, starting from a population with several individuals, then among them, some are selected based on some criteria (e. g., scores, ...) and used for reproduction. 

<p align="center">
  <img  width="600" height="200" src="https://github.com/MossyFighting/Optimization/blob/master/images/GA_general.png" />
</p>

The reproduction process is comprised of many steps, selected pair (or many pairs) interact(s) with each other, producing some offsprings by using some methods (i.g., crossover), mutate some genes with hope to create superb genes if possible (i. g., flip gene if some conditions are satisfied), and reassure only mixed traits of those pairs actually better than pair(s) themself by comparision them with their mixed genes. 

Finally, the population is updated by adding some new and superb gene or still keep the old ones if the new one is not as expected. Then the loop is continuing until some criteria are met and stop. 

Summary, the natural process can be seen as a 6-step procedure, specifically:
1. Population initialization 
2. Fitness 
3. Selection 
4. Interation (e.g., Cross-over)
5. Offsprings production (e.g., mutation)
6. Elitism and update population 

# 3. Analysis Genetic algorithm
## 3.1 Population initialization 
The population represents for a group of individuals among them each individual is the possible solution to the problem we are interested in. Indeed, one of them will be the final solution. 

One individual is represented by a chromosome that are encoded by a string of genes. Gene can be considered the smallest part and can not break into smaller. Chromosome is also be seen as unknowns that needed to be found. Although unknowns by values, but the length and the range of each gene will be decided by human-being. 

<p align="center">
  <img   src="https://github.com/MossyFighting/Optimization/blob/master/images/Population_fitness.png" />
</p>

The gene can be defined in many different ways depending on the real problem that one is facing. For example:
* If the problem related to binary variable: gene is {0, 1},
* If the problem related to integer variable: gene is {0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
* If the problem related to alphabet variable: gene is {A, B, C, D, ...., X, Y, Z},
* and so on

## 3.2 Fitness
The fitness plays an important role in the GA. It wil tell how well each individual in the population is. Fitness often assocciated to fitness function that give a specific 'score' to each individual and thereafter the highest score is often considered as the winner in competition. In another word, fitness is also related to the possibility that each individual has after some manipulation.   

For example, in the competition between many players in a race 100 meter length, the fitness is the time for each player to finish that race line. Therefore, a player finish that race line in 10 seconds will have the fitness higer than any player pass the destination line in 11 seconds or more.

## 3.3 Selection
Selection is a phase where pair or more pairs with good traits or characters are selected and pass their good characteristics on their next generation. The pairs are chosen based on their fitness. The more fitness score, the higer probability the pairs are selected for later use to produce better solution.

There are many selections methods can be used such as: truncation selection, tournament selection, and so on. However, for the sake of simplicity, the figure below just show a simplest or naive way in which two individuals with highest score are chosen.

<p align="center">
  <img   src="https://github.com/MossyFighting/Optimization/blob/master/images/fitness.png" />
</p>

Indeed, the population is comprised of five individuals (e.g., I1, I2, I3, I4, and I5), and then fitness scores are computed. As we can see, the second and fourth individuals have the highest scores among them.  Then the pair (I2, I4) are picked for reproduction new offsprings. 

## 3.4 Crossover
Crossover is the most important stage of the GA for the pair in Selection phase to interact and produce new children. As we can see from the figure, the cross point is chosen randomly within the range length of chromosome (e.g. in this case number of gene is eight), and then each part of pair is exchanged then form two new offsprings. 

<p align="center">
  <img   src="https://github.com/MossyFighting/Optimization/blob/master/images/Crossover.png" />
</p>

For example, in the I2 (second individual chosen from previous step), left part from cross point is exchanged with the first part of I4 (the fourth parent selected from Selection phase), then two offsprings I2_new and I4_new are generated.

## 3.5 Mutation
Mutation is the idea of mutating some genes of new born entity with the hope that this entity become superb, much better than their parents. To do that, a random number according to each of gene is generated and if gene random number is less than a very small defined number then that gene is flipped to change its state. 
The reason for choosing small defined number is that, the superb child to create is not so many, then this number should be small to make it more sense.

<p align="center">
  <img   src="https://github.com/MossyFighting/Optimization/blob/master/images/Mutation.png" />
</p>

For example, in the figure the second, fifth and eighth gene of I2_new are flipped to form a new entity I2_mu. 

## 3.6 Elitism and update population
Elitism is an important phase to double check between the old parents, the individuals in the population and the new born children created. Because it is not sure that the mixed genes between best fitness pair(s) always results in superb children. Then, with elitism, one reassure that the good traits still prevail in the population instead of being eliminated. That is indeed a good practice for the GA. 

# 4. The GA in pseudocode 

BEGIN GA<br/>
Initialize population<br/>
Compute fitness<br/>
LOOP UNTIL<br/>

* Crossover
* Mutation
* Compute fitness
* Elitism

TERMINATION is satisfied<br/>
END

# 5. Verification Example
In this verification step, we will define a problem and check whether our algorithm can work or not. If it works, how optimal the results are, optimal or sub-optimal.

## 5.1 problem statement
The problem we would like to solve is related to the binary variable, with length of ten genes. Cost or fitness function can be defined as follows:
we would like to minimize the function:

<img src="https://render.githubusercontent.com/render/math?math=f(x) = 1.1 \times x_1 %2B 1.7 \times x_2 - 2.2 \times x_3 - 1.6 \times x_4 %2B 0.4 \times x_5 - 3.1 \times x_6 %2B 4.3 \times x_7 - 0.1 \times x_8 - 3.5 \times x_9 %2B 2.4 \times x_10">

And the condition is each element of <img src="https://render.githubusercontent.com/render/math?math= x = [ x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10 ]"> must be 0 or 1. 

## 5.2 results 
Execute the file 'gA.py' with setting number of iteration 40. We can see that at each iteration, the fitness value is decreased to smaller. And finally, it saturated when reaching minimum fitness at -10.5 with x =[0, 0, 1, 1, 0, 1, 0, 1, 1, 0].

<p align="center">
  <img   src="https://github.com/MossyFighting/Optimization/blob/master/images/run_example.png" />
</p>

## Verify the results by using brute force method

From the file 'verification_solution.py', because variable x contain 10 state (<img src="https://render.githubusercontent.com/render/math?math= x = [ x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10 ]">) and each state have only two variable 0 or 1. Therefore, in total we will have (<img src="https://render.githubusercontent.com/render/math?math=2^10 = 1024 ]">) possible solutions. 

By using the brute force method, we go through all possible solution, compute all possible fitnesses. Then, filter out the minimum value, and double check with the results returning from the GA. 

<p align="center">
  <img  width="600" height="200" src="https://github.com/MossyFighting/Optimization/blob/master/images/verification_result.png" />
</p>

Indeed, from the figure, we can confirm that the solution in using brute force method give us the same minimum fitness at x =[0, 0, 1, 1, 0, 1, 0, 1, 1, 0] compared to the ones in the GA method.


