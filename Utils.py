class P2D:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    @property
    def as_tuple(self):
        return self.x, self.y

    @property
    def onedirectional(self):
        return self.x == 0 or self.y == 0

    @property
    def len(self):
        return abs(self.x) + abs(self.y)

    def move(self, x: int, y: int):
        self.x += x
        self.y += y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return other is None or (self.x != other.x or self.y != other.y)

    def __add__(self, other):
        return P2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, P2D):
            return P2D(self.x * other.x, self.y - other.y)
        elif isinstance(other, (float, float)):
            return P2D(self.x * other[0], self.y - other[1])

    def __truediv__(self, other):
        if isinstance(other, P2D):
            return P2D(self.x / other.x, self.y / other.y)
        elif isinstance(other, (float, float)):
            return P2D(self.x / other[0], self.y / other[1])

    def __str__(self):
        return "P2D(" + str(self.x) + ", " + str(self.y) + ")"


def flat_map(f, xs):
    ys = []
    for x in xs:
        ys.extend(f(x))
    return ys

def points_in_between(p1: P2D, p2: P2D) -> list[P2D]:
    change = p2 - p1
    res = []
    for i in range(abs(change.x)):
        res.append(p1 + P2D(i, 0))
    for i in range(abs(change.y)):
        res.append(p1 + P2D(0, i))
    res.append(p2)
    return res