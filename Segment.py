import math
from Board import Board
from Utils import P2D


def ccw(a: P2D, b: P2D, c: P2D) -> bool:
    return (c.y - a.y) * (b.x - a.x) >= (b.y - a.y) * (c.x - a.x)


def intersect(a, b, c, d) -> bool:
    return (a.x <= c.x <= b.x and a.x <= d.x <= b.x or b.x <= c.x <= a.x and b.x <= d.x <= a.x) and \
           (a.y <= c.y <= b.y and a.y <= d.y <= b.y or b.y <= c.y <= a.y and  b.y <= d.y <= a.y)
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


class Segment:
    def __init__(self, start: P2D, end: P2D):
        self.end = end
        self.start = start

    def crosses(self, segment) -> bool:
        return intersect(self.start, self.end, segment.start, segment.end)

    def is_fully_outside(self, board: Board) -> bool:
        return (self.start.x < 0 and self.end.x < 0) or (self.start.y < 0 and self.end.y < 0)\
               or (self.start.x >= board.size.x and self.end.x >= board.size.x) \
               or (self.start.y >= board.size.y and self.end.y >= board.size.y)

    def get_distance_outside(self, board: Board) -> float:
        if self.start.x < 0 <= self.end.x:
            return abs(self.start.x)
        if self.start.y < 0 <= self.end.y:
            return abs(self.start.y)
        if self.end.x < 0 <= self.start.x:
            return abs(self.end.x)
        if self.end.y < 0 <= self.start.y:
            return abs(self.end.y)
        if self.start.x < board.size.x <= self.end.x:
            return self.end.x - board.size.x
        if self.start.y < board.size.x <= self.end.y:
            return self.end.y - board.size.x
        if self.end.x < board.size.y <= self.start.x:
            return self.start.x - board.size.y
        if self.end.y < board.size.y <= self.start.y:
            return self.start.y - board.size.y
        return 0

    @property
    def change(self) -> P2D:
        return self.end - self.start

    @property
    def length(self) -> float:
        return abs(self.change.x) + abs(self.change.y)

    @property
    def direction(self) -> P2D:
        return P2D(math.copysign(1, self.change.x), math.copysign(1, self.change.y))

    def __str__(self):
        return "Segment(" + str(self.direction) + ", " + str(self.length) + ")"