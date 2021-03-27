from Population import Population
from stats import get_stats, best, worst


class Result:
    def __init__(self, population: Population):
        self.population = population
        self.stats = get_stats(population)
        self.best_solution = best(population)
        self.worst_solution = worst(population)
