#!/usr/bin/env python3

from heapq import *

fname = "input.txt"
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]
dat = [[*map(int, iter(x))] for x in dat]


def neighbors(d, x, y):
    lenx = len(d)
    leny = len(d[0])
    for a, b in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if 0 <= a < lenx and 0 <= b < leny:
            yield a, b


def find_risk(d):
    risk = [[2**31 for _ in x] for x in d]
    risk[0][0] = 0

    todo = [(0, (0, 0))]
    while todo:
        _, (x, y) = heappop(todo)
        for a, b in neighbors(d, x, y):
            if risk[a][b] > d[a][b] + risk[x][y]:
                risk[a][b] = d[a][b] + risk[x][y]
                heappush(todo, (risk[a][b], (a, b)))
    return risk[-1][-1]


def extend_cave(d):
    lenx = len(d)
    leny = len(d[0])
    return [[(d[x % lenx][y % leny] + x//lenx + y//leny - 1) % 9 + 1 \
            for y in range(5*leny)] for x in range(5*lenx)]


print(find_risk(extend_cave(dat))) 

