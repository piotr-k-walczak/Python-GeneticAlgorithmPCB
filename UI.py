import random

import matplotlib.pyplot as plt
from matplotlib.path import Path as MatPlot
import matplotlib.patches as patches
from Solution import Solution
from Path import Path


def showPlot(solution: Solution):
    fig, ax = plt.subplots()

    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)

    fig, ax = plt.subplots()

    def singlePlot(path: Path):
        rgb = (random.random(), random.random(), random.random(), 0.3)
        verts = [p.as_tuple for p in path.points]

        codes = [MatPlot.LINETO for _ in verts]
        codes[0] = MatPlot.MOVETO

        path = MatPlot(verts, codes)

        patch = patches.PathPatch(path, facecolor=rgb, lw=2)
        ax.add_patch(patch)

        xs, ys = zip(*verts)
        ax.plot(xs, ys, 'x--', lw=2, ms=10)

    print(len(solution.paths))
    for p in solution.paths:
        singlePlot(p)

    plt.show()


def showResPerGenPlot(scores: [(float, float, float, float)]):
    # Data for plotting
    b = [s[0] for s in scores]
    w = [s[1] for s in scores]
    a = [s[2] for s in scores]

    fig, ax = plt.subplots()
    ax.plot(b)
    ax.plot(w)
    ax.plot(a)

    ax.set(xlabel='Generation', title='Results per generation')
    ax.grid()

    plt.show()