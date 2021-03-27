from loadData import loadData


class Board:
    def __init__(self, path):
        sz, points = loadData(path)
        self.size = sz
        self.conn_points = points

    def printStatus(self):
        for (p1, p2) in self.conn_points:
            print(p1)
            print(p2)