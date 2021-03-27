from typing import List
from Utils import P2D
from connect import connect_two_points


def correct(points: List[P2D]) -> List[P2D]:
    corrected = []
    for i in range(1, len(points)):
        change = points[i] - points[i - 1]
        if not change.onedirectional:
            corrected.extend(
                connect_two_points(points[i - 1], points[i], directly=True, previous=None if i == 1 else corrected[-1])[
                :-1])
        else:
            corrected.append(points[i - 1])
    corrected.append(points[-1])
    return remove_repeated(corrected)


def remove_repeated(points: List[P2D]) -> List[P2D]:
    corrected = points[:2]
    for i in range(2, len(points)):
        change = corrected[-1] - corrected[-2]
        change2 = points[i] - corrected[-1]
        if (change.x == change2.x == 0) or (change.y == change2.y == 0):
            corrected[-1] = points[i]
        else:
            corrected.append(points[i])
    return corrected
