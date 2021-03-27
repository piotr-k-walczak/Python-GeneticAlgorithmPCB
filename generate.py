import math
import random
from typing import List

from Board import Board
from Population import Population
from Config import POPULATION
from Solution import Solution
from Path import Path
from Utils import P2D
from correct import correct


def generate_population(board: Board) -> Population:
    return Population([generate_solution(board) for _ in range(POPULATION)])


def generate_solution(board: Board) -> Solution:
    paths = []
    for (s, e) in board.conn_points:
        p = generate_path(board, s, e)
        paths.append(p)
    return Solution(paths)


def generate_path(board: Board, start: P2D, end: P2D) -> Path:
    path = Path(start, end)
    points = [start]
    # points.extend(generate_random_points(board, start, end))
    points.extend(generate_random_points(board))
    points.append(end)
    path.points = correct(points)
    return path


def generate_random_points(board: Board, amount=random.randint(8, 15)) -> List[P2D]:
    return [generate_random_point(board) for _ in range(4, amount)]


def generate_random_point(board: Board) -> P2D:
    return P2D(random.randint(0, board.size.x), random.randint(0, board.size.y))


def generate_semi_random_points(board: Board, start: P2D, end: P2D) -> List[P2D]:
    res = []
    remaining = end - start
    if remaining.x == 0:
        while remaining.y != 0:
            res.append(generate_semi_random_point(board, res[-1] if len(res) > 0 else start, end, horizontal=False))
            remaining = end - res[-1]
    else:
        while remaining.x != 0:
            res.append(generate_semi_random_point(board, res[-1] if len(res) > 0 else start, end))
            remaining = end - res[-1]
    return res


def generate_semi_random_point(board:Board, start: P2D, end: P2D, horizontal=True) -> P2D:
    remaining = end - start
    if horizontal:
        point = P2D(start.x + math.copysign(1, remaining.x) * random.randint(1, abs(remaining.x)), random.randint(0, board.size.x))
    else:
        point = P2D(random.randint(0, board.size.y), start.y + math.copysign(1, remaining.y) * random.randint(1, abs(remaining.y)))
    return point

