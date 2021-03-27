from copy import deepcopy

from Board import Board
from Path import Path
from Utils import flat_map, P2D, points_in_between


class Solution:
    def __init__(self, paths=[]):
        self.paths: list[Path] = paths
        self.score: float = None
        self.layout: list[list[int]] = [[]]

    @property
    def length(self) -> int:
        return sum([p.length for p in self.paths])

    @property
    def number_of_segments(self) -> int:
        return sum([p.number_of_segments for p in self.paths])

    def number_of_crosses(self, board: Board) -> int:
        self.layout = [[0 for _ in range(board.size.y + 1)] for _ in range(board.size.x + 1)]
        for p in self.paths:
            for i in range(len(p.points) - 1):
                for pt in points_in_between(p.points[i], p.points[i + 1]):
                    if 0 <= pt.x <= board.size.x and 0 <= pt.y <= board.size.y:
                        self.layout[pt.x][pt.y] += 1
        return sum([max(0, p - 1) for p in flat_map(lambda x: x, self.layout)])

    def get_distance_outside(self, board: Board) -> int:
        return sum([int(p.get_distance_outside(board)) for p in self.paths])

    def get_segments_fully_outside(self, board: Board) -> int:
        return sum([int(p.get_segments_fully_outside(board)) for p in self.paths])

    def print(self):
        print("Solution: (")
        for p in self.paths:
            p.print()
        print(") End Solution")

