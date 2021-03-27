import math
import random
from random import randint
import sys
from typing import List

from Utils import P2D


def connect_two_points(start: P2D, end: P2D, directly=False, previous: P2D = None) -> List[P2D]:
    points = [start]
    remaining = end - points[-1]
    #    i = 0
    while remaining.x != 0 or remaining.y != 0:
        remaining = end - points[-1]
        axis = randint(0, 1)

        if remaining.x != 0 and (axis == 0 or remaining.y == 0):
            change = randint(1, abs(remaining.x)) if not directly else abs(remaining.x)
            point = points[-1] + P2D(math.copysign(1, remaining.x) * change, 0)
        elif remaining.y != 0 and (axis == 1 or remaining.x == 0):
            change = randint(1, abs(remaining.y)) if not directly else abs(remaining.y)
            point = points[-1] + P2D(0, math.copysign(1, remaining.y) * change)
        if point != points[-1]:
            points.append(point)

    return points
