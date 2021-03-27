import copy
import random
from Board import Board
from Population import Population
from UI import showPlot, showResPerGenPlot
from Selectors import select_two
from generate import generate_population
from mutate import mutate
from crossover import crossover
from score import score_population
from stats import get_stats, best, worst
from Config import *
from Config import SEED

if __name__ == "__main__":
    random.seed(SEED)

    board = Board(DATA_PATH)
    population = generate_population(board)
    score_population(board, population)
    best_score, worst_score, avg_score, std_score = get_stats(population)

    scores_per_gen = []

    i = 1
    no_change = 0
    while i <= GENERATIONS and no_change < STOP_AFTER:
        if no_change == 0:
            score_population(board, population)
            best_score, worst_score, avg_score, std_score = get_stats(population)
        scores_per_gen.append((best_score, worst_score, avg_score, std_score))
        print(str(i) + ". Best: " + str(best_score) + ", Worst: " + str(worst_score) + ", Avg: " + str(avg_score) + ", Std: " + \
              str(std_score))

        new_population = Population()
        new_population.solutions = []
        while len(new_population.solutions) < POPULATION:
            p1, p2 = select_two(population.solutions)
            if random.random() < CROSSOVER_PROBABILITY:
                o1, o2 = crossover(p1, p2)
                o1.score = o2.score = None
                o1 = mutate(o1)
                o2 = mutate(o2)
                new_population.add(o2)
            else:
                o1 = copy.deepcopy(p1)
                o1.score = None
                o1 = mutate(o1)
            new_population.add(o1)

        new_population.solutions = new_population.solutions[:POPULATION]
        score_population(board, new_population)
        new_best_score = best(new_population).score

        if new_best_score < best_score:
            population = new_population
            no_change = 0
        else:
            no_change += 1

        i+=1

    if no_change == 0:
        score_population(board, population)
        best_score, worst_score, avg_score, std_score = get_stats(population)

    print(str(scores_per_gen))
    showResPerGenPlot(scores_per_gen)
    print("\n\n---SUMMARY---")
    print("Best: " + str(best_score) + ", Worst: " + str(worst_score) + ", Avg: " + str(avg_score) + ", Std: " + str(std_score))
    print("---BEST SOLUTION---")
    b = best(population)
    b.print()
    showPlot(b)
    print("---WORST SOLUTION---")
    w = worst(population)
    showPlot(w)
