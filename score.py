from typing import List
from Population import Population
from Solution import Solution
from Board import Board
from Config import *


def score(board: Board, solution: Solution) -> float:
    score_res = 0
    score_res += LENGTH_WEIGHT * solution.length
    score_res += SEGMENT_WEIGHT * solution.number_of_segments
    score_res += CROSSING_WEIGHT * solution.number_of_crosses(board)
    score_res += DISTANCE_OUTSIDE_WEIGHT * solution.get_distance_outside(board)
    score_res += FULL_SEGMENT_OUTSIDE_WEIGHT * solution.get_segments_fully_outside(board)
    return score_res


def score_list(board: Board, solutions: List[Solution]) -> List[Solution]:
    for solution in solutions:
        solution.score = score(board, solution)
    return solutions


def score_population(board: Board, population: Population) -> Population:
    score_list(board, population.solutions)
    return population
