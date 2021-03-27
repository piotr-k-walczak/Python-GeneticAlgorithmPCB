import math
from typing import List
from Population import Population
from Solution import Solution


def best_from_list(solutions: List[Solution]) -> Solution:
    best_res = solutions[0]
    for s in solutions:
        if s.score < best_res.score:
            best_res = s
    return best_res


def best(population: Population) -> Solution:
    return best_from_list(population.solutions)


def total_score_from_list(solutions: List[Solution]) -> float:
    return sum([s.score for s in solutions])


def total_score(population: Population) -> float:
    return total_score_from_list(population.solutions)


def worst_from_list(solutions: List[Solution]) -> Solution:
    worst_res = solutions[0]
    for s in solutions:
        if s.score > worst_res.score:
            worst_res = s
    return worst_res


def worst(population: Population) -> Solution:
    return worst_from_list(population.solutions)


def avg(population: Population) -> float:
    return sum([s.score for s in population.solutions]) / len(population.solutions)


def std(population: Population) -> float:
    mean = avg(population)
    return math.sqrt(sum(math.pow(s.score - mean, 2) for s in population.solutions) / len(population.solutions))


def get_stats(population: Population) -> (float, float, float, float):
    return best(population).score, worst(population).score, avg(population), std(population)