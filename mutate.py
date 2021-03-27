import math
import random
from copy import deepcopy

from Solution import Solution
from Config import MUTATION_PROBABILITY, SEED, DATA_PATH
from Board import Board
from UI import showPlot
from generate import generate_solution
from correct import correct


def mutate(solution: Solution):
    for path in solution.paths:
        if random.random() < MUTATION_PROBABILITY:
            if len(path.points) > 3:
                change_point = random.randint(1, len(path.points) - 3)
                change_x = random.randint(0, 1)
                dir = 1 - 2 * random.randint(0, 1)
                path.points[change_point].move(dir * change_x, dir * (1 - change_x))
                if random.randint(0, 1) == 0:
                    path.points[change_point + 1].move(dir * change_x, dir * (1 - change_x))
            else:
                change = path.points[1] - path.points[0]
                if change.x == 0:
                    if abs(change.y) > 1:
                        change.x = 1 - 2 * random.randint(0, 1)
                        change.y = math.copysign(1, change.y) * random.randint(1, abs(change.y))
                elif change.y == 0:
                    if abs(change.x) > 1:
                        change.y = 1 - 2 * random.randint(0, 1)
                        change.x = math.copysign(1, change.x) * random.randint(1, abs(change.x))
                path.points.insert(1, path.points[0] + change)
        path.points = correct(path.points)
    return solution
