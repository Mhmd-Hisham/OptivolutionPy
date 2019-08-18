# Simple-GA
A flexible genetic algorithm framework written in Python3.

## Installation

For python3, simply run:
```sh
$ pip3 install simple-ga

```

Or clone this repository and run python3 setup.py install from within the project directory. e.g.:
```sh
$ git clone https://github.com/Mhmd-Hisham/Simple-GA.git
$ cd simple-ga
$ python3 setup.py install
```

## Examples
### Solving the one-dimensional [knapsack problem](http://en.wikipedia.org/wiki/Knapsack_problem):

```python3
#!/usr/bin/env python3

import random

from simple-ga.Population import Population
from simple-ga.Chromosome import Chromosome

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

    # The optimal answer for test case is
    # (15, [0, 1, 1, 1, 1])
    print((best.fitness, best.genes))

if __name__ == "__main__":
    main()
```

Output:
```
(15, [0, 1, 1, 1, 1])
```

### Solving the multi-dimensional [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem#Multi-dimensional_knapsack_problem):

```python3
#!/usr/bin/env python3

import random

from simple-ga.Population import Population
from simple-ga.Chromosome import Chromosome

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
```

Output: (might vary since we are using a GA)
```
(3531, [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1])
```

## Advanced Example
[![SmartAnts](http://img.youtube.com/vi/f1ZrNOkd1Zw/0.jpg)](http://www.youtube.com/watch?v=f1ZrNOkd1Zw "Smart Ants Using Simple-GA in Processing3")


## License

This project is licensed under the GNU GPLv3 License - check [LICENSE](LICENSE) for more details.
