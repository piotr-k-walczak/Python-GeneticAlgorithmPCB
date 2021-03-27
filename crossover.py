import random
from copy import deepcopy
from typing import List

from Solution import Solution
from Path import Path


def crossover(solution1: Solution, solution2: Solution) -> (Solution, Solution):
    m = min(len(solution1.paths), len(solution2.paths)) - 1
    copy1 = deepcopy(solution1)
    copy2 = deepcopy(solution2)
    if m > 1:
        change_point = random.randint(0, m)
        swap_from(copy1.paths, copy2.paths, change_point+1)
        crossovers = crossover_paths(copy1.paths[change_point], copy2.paths[change_point])
        copy1.paths[change_point] = crossovers[0]
        copy2.paths[change_point] = crossovers[1]
    return copy1, copy2


def crossover_paths(path1: Path, path2: Path) -> (Path, Path):
    m = min(len(path1.points), len(path2.points)) - 2
    copy1 = deepcopy(path1)
    copy2 = deepcopy(path2)
    if m > 1:
        change_point = random.randint(1, m)
        swap_from(copy1.points, copy2.points, change_point)
    return copy1, copy2


def swap_from(list1: List, list2: List, point: float):
    tmp = list2[point:]
    list2[point:] = list1[point:]
    list1[point:] = tmp
