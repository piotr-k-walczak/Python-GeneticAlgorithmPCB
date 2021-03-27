import random
from Board import Board
from Config import SEED
from generate import generate_population, generate_solution
from score import score_population
from stats import get_stats, best, worst
from UI import showPlot

if __name__ == "__main__":
    random.seed(SEED)

    board = Board("data/zad0.txt")
    board.printStatus()

    population = generate_population(board)
    score_population(board, population)
    best_score, worst_score, avg_score, std_score = get_stats(population)

    print("\n\n---SUMMARY---")
    print("Best: " + str(best_score) + ", Worst: " + str(worst_score) + ", Avg: " + str(avg_score) + ", Std: " + str(std_score))
    b = best(population)
    b.print()
    showPlot(b)
    w = worst(population)
    w.print()
    showPlot(w)

