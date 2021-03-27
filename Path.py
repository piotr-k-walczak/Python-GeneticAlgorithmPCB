from typing import List

from Segment import Segment
from Utils import P2D
from Board import Board


class Path:
    def __init__(self, start, end):
        self._points: list[P2D] = [start]
        self._length: float = self._calc_length()
        self.segments = self._to_segments()
        self.end: P2D = end

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, new_value):
        self._points = new_value
        self._length: float = self._calc_length()
        self.segments = self._to_segments()

    @property
    def start(self):
        return self.points[0]

    @property
    def number_of_segments(self):
        return len(self.points) - 1

    @property
    def length(self):
        return self._length

    def _calc_length(self):
        res = 0
        for i in range(1, len(self.points)):
            res += (self.points[i] - self.points[i - 1]).len
        return res

    def _to_segments(self) -> List[Segment]:
        res = []
        for i in range(1, len(self.points)):
            res.append(Segment(self.points[i - 1], self.points[i]))
        return res

    def number_of_crosses_with(self, path):
        res = 0
        for i in range(len(self.segments)):
            for j in range(len(path.segments)):
                res += int(self.segments[i].crosses(path.segments[j]))
        return res

    def get_segments_fully_outside(self, board: Board):
        return sum([int(s.is_fully_outside(board)) for s in self.segments])

    def get_distance_outside(self, board: Board):
        return sum([int(s.get_distance_outside(board)) for s in self.segments])

    def print(self):
        print("Path: (")
        print(" -> ".join([str(p) for p in self.points]))
        print(") End Path")