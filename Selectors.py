from random import random, shuffle
import random
from typing import List
from Board import Board
from Config import TOURNAMENT_SIZE, SELECTION_TYPE, SelectionType
from Solution import Solution
from score import score
from stats import best_from_list, total_score_from_list
from Population import Population


def select_by_tournament(solutions: List[Solution]) -> Solution:
    selected = random.choices(solutions, k=TOURNAMENT_SIZE)
    best_res = best_from_list(selected)
    return best_res


def select_by_roulette(solutions: List[Solution]) -> Solution:
    selected = random.choices(solutions, weights=[s.score for s in solutions], k=TOURNAMENT_SIZE)
    best_res = best_from_list(selected)
    return best_res


def select(solutions: List[Solution]) -> Solution:
    if SELECTION_TYPE == SelectionType.TOURNAMENT:
        return select_by_tournament(solutions)
    return select_by_roulette(solutions)


def select_two(solutions: List[Solution]) -> (Solution, Solution):
    s1 = select(solutions)
    second_pool: List[Solution] = []
    second_pool.extend(solutions)
    second_pool.remove(s1)
    return s1, select(second_pool)

