from Utils import P2D


def loadData(path='data/zad0.txt'):
    file = open(path, "r")
    [x, y] = file.readline().split(";")
    size = P2D(int(x), int(y))
    conn_points = []
    for line in file:
        params = line.split(";")
        conn_points.append((P2D(params[0], params[1]), P2D(params[2], params[3])))
    return size, conn_points
