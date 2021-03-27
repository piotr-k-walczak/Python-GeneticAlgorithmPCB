import copy
import random
from Board import Board
from Population import Population
from Solution import Solution
from Result import Result
from score import score_population
from Config import *
from Config import SEED


def process() -> Result:
    random.seed(SEED)
    board = Board(DATA_PATH)
    population = Population.generate_random_population(board, POPULATION)

    for gen in range(GENERATIONS):
        score_population(board, population)

        new_population = Population()
        for _ in range(len(population.solutions)):
            p1, p2 = population.select_two()
            if random.random() > CROSSOVER_PROBABILITY:
                o1 = Solution.generate_from_crossover(p1, p2)
            else:
                o1 = copy.deepcopy(p1)
            o1.mutate(random.random())
            new_population.add(o1)

        population = new_population

    score_population(board, population)
    return Result(population)
