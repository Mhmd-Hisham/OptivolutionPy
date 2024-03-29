#!/usr/bin/env python3
"""
    OptivolutionPy example project.
    Solving the One-dimensional knapsack problem.
"""

import random

from optivolution.population import Population
from optivolution.chromosome import Chromosome

class OneDimensinalKnapsack(Chromosome):
    """ Inidividual knapsack object. """
    maximum_weight = 15
    knapsack_data = [{'name': 'box1', 'value': 4, 'weight': 12},
                     {'name': 'box2', 'value': 2, 'weight': 1},
                     {'name': 'box3', 'value': 10, 'weight': 4},
                     {'name': 'box4', 'value': 1, 'weight': 1},
                     {'name': 'box5', 'value': 2, 'weight': 2}]
    
    def __init__(self, genes_length=len(knapsack_data), genes=[]):
        super().__init__(genes_length, genes)
    
    @Chromosome.fitness_property
    def fitness(self):        
        """ Defining the fitness function. """
        # Use the knapsack value as the fitness value
        total_value = 0
        total_weight = 0
        
        for i in range(self.genes_length):
            if (self.genes[i] == True):
                total_value += self.knapsack_data[i]['value']
                total_weight += self.knapsack_data[i]['weight']
        
        if total_weight > self.maximum_weight:
            total_value = 0
        
        return total_value
    
    def random_gene(self):
        """ Defining the random gene. """
        return random.choice((0, 1))

class KnapscakPopulation(Population):
    tournament_sample_percentage = 10

    def random_individual(self):
        """ Defining the random individual in the population. """
        return OneDimensinalKnapsack()

def main():
    population = KnapscakPopulation(population_size=20)
    
    population.run(20)
    
    print(f"Generation {population.generation_number}")
    
    best = population.get_best_individual()

    # The optimal answer for this test case is
    # (15, [0, 1, 1, 1, 1])
    print((best.fitness, best.genes))

if __name__ == "__main__":
    main()
