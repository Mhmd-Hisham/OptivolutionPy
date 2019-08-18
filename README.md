# OptivolutionPy
A flexible genetic algorithm library written in Python3.

## Installation

For python3, simply run:
```sh
$ pip3 install OptivolutionPy

```

Or clone this repository and run python3 setup.py install from within the project directory. e.g.:
```sh
$ git clone https://github.com/Mhmd-Hisham/OptivolutionPy.git
$ cd OptivolutionPy
$ python3 setup.py install
```

## Examples
### Solving the one-dimensional [knapsack problem](http://en.wikipedia.org/wiki/Knapsack_problem):

```python3
#!/usr/bin/env python3

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

## Advanced Example
#### Smart Ants using OptivolutionPy & Processing3. check this [repo](https://github.com/Mhmd-Hisham/SmartAntsGA) for more details.


[![SmartAnts](http://img.youtube.com/vi/f1ZrNOkd1Zw/0.jpg)](http://www.youtube.com/watch?v=f1ZrNOkd1Zw "Smart Ants Using OptivolutionPy in Processing3")


## License

This project is licensed under the GNU GPLv3 License - check [LICENSE](LICENSE) for more details.
