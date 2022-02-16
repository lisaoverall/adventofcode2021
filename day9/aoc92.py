#!/usr/bin/env python3

from functools import reduce
from itertools import product

fname = "test.txt"
with open(fname) as f:
    dat = f.readlines()

class Point:
    def __init__(self, val):
        self.val = val
        self.visited = False

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __gt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return "({}, {})".format(self.val, self.visited)

    def visit(self):
        self.visited = True

dat = [list(map(lambda x: Point(int(x)), list(d.strip()))) for d in dat]

ymax = len(dat) - 1
xmax = len(dat[0]) - 1


def neighbors(y, x):
 
    up = (y-1, x)
    down = (y+1, x) 
    left = (y, x-1)
    right = (y, x+1)

    if y == 0:
        if x == 0:
            neighbors = [right, down]
        elif x == xmax:
            neighbors = [left, down]
        else:
            neighbors = [left, right, down]
    elif y == ymax:
        if x == 0:
            neighbors = [right, up]
        elif x == xmax:
            neighbors = [left, up]
        else:
            neighbors = [left, right, up] 
    else:
        if x == 0:
            neighbors = [up, down, right]
        elif x == xmax:
            neighbors = [up, down, left]
        else:
            neighbors = [up, down, left, right]

    return neighbors

def is_low_point(y, x):
    ns = neighbors(y, x)
    p = dat[y][x]
    return all([p < dat[i][j] for (i, j) in ns])


def basin_size(y, x):

    def help(y, x):
        p = dat[y][x]
        if p.visited or p.val == 9:
            return 0
        p.visit()
        return 1 + sum(map(lambda x: help(x[0], x[1]), neighbors(y, x)))

    p = dat[y][x]
    p.visit()
    return 1 + sum(map(lambda x: help(x[0], x[1]), neighbors(y, x)))

low_points = filter(lambda t: is_low_point(t[0], t[1]), product(range(ymax+1), range(xmax+1)))
basins = map(lambda t: basin_size(t[0], t[1]), low_points)
basins_largest = sorted(basins, reverse=True)[:3]
print(reduce(lambda x, y: x*y, basins_largest))
