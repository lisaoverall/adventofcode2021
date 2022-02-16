#!/usr/bin/env python3

import numpy as np
import sys

fname = "input.txt"
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

def do_fold(pts, axis, dist):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    if axis == 'x':  # fold left
        xs = [dist - (x-dist) if x > dist else x for x in xs]
        pts = list(zip(xs, ys))
    else:  # axis == y, fold up
        ys = [dist - (y-dist) if y > dist else y for y in ys]
        pts = list(zip(xs, ys))

    return pts

pts = []
for d in dat:
    if "," in d:
        x, y = d.split(",")
        pts.append((int(x), int(y)))
    elif "fold" in d:
        f = d.split(" ")[-1]
        axis, dist = f.split("=")
        dist = int(dist)
        pts = do_fold(pts, axis, dist)
    else:
        pass

xmin = min([p[0] for p in pts])
xmax = max([p[0] for p in pts])
ymin = min([p[1] for p in pts])
ymax = max([p[1] for p in pts])

arr = np.zeros((ymax+1-ymin,xmax+1-xmin))
for x, y in pts:
    arr[y-ymin,x-xmin] = 1
for r in arr:
    r = ["#" if x else '.' for x in r]
    print("".join(r))
