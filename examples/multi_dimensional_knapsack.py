#!/usr/bin/env python3
"""
    OptivolutionPy example project.
    Solving the Multi-dimensional knapsack problem.
"""

import random

from optivolution.population import Population
from optivolution.chromosome import Chromosome

class MultiDimensinalKnapsack(Chromosome):
    """ Inidividual knapsack object. """
    maximum_weight = 12210
    maximum_volume = 12
    knapsack_data = [(821, 0.8, 118), (1144, 1, 322), (634, 0.7, 166), (701, 0.9, 195),
                     (291, 0.9, 100), (1702, 0.8, 142), (1633, 0.7, 100), (1086, 0.6, 145),
                     (124, 0.6, 100), (718, 0.9, 208), (976, 0.6, 100), (1438, 0.7, 312),
                     (910, 1, 198), (148, 0.7, 171), (1636, 0.9, 117), (237, 0.6, 100),
                     (771, 0.9, 329), (604, 0.6, 391), (1078, 0.6, 100), (640, 0.8, 120),
                     (1510, 1, 188), (741, 0.6, 271), (1358, 0.9, 334), (1682, 0.7, 153),
                     (993, 0.7, 130), (99, 0.7, 100), (1068, 0.8, 154), (1669, 1, 289)]    

    def __init__(self, genes_length=len(knapsack_data), genes=[]):
        super().__init__(genes_length, genes)
    
    @Chromosome.fitness_property
    def fitness(self):
        """ Defining the fitness function.
            The fitness is calculated as the total price in this problem.
        """
        weight, volume, price = 0, 0, 0
        for i in range(self.genes_length):
            if self.genes[i]:
                weight += self.knapsack_data[i][0]
                volume += self.knapsack_data[i][1]
                price += self.knapsack_data[i][2]

        if weight > self.maximum_weight or volume > self.maximum_volume:
            price = 0

        return price

    def random_gene(self):
        """ Defining the random gene. """
        return random.choice((0, 1))

class KnapscakPopulation(Population):
    tournament_sample_percentage = 2.5

    def random_individual(self):
        """ Defining the random individual in the population. """
        return MultiDimensinalKnapsack()

def main():
    population = KnapscakPopulation(population_size=200)
    
    population.run(100)
    
    print(f"Generation {population.generation_number}")
    
    best = population.get_best_individual()
    
    # The optimal answer for this test case is
    # (3531, [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1])
    print((best.fitness, best.genes))

if __name__ == "__main__":
    main()
