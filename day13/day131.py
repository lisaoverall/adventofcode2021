#!/usr/bin/env python3

fname = "input.txt"
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

def do_fold(pts, axis, dist):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    if axis == 'x':  # fold left
        xs = [x - 2*(x-dist) if x > dist else x for x in xs]
        pts = list(zip(xs, ys))
    else:  # axis == y, fold up
        ys = [y - 2*(y-dist) if y < dist else y for y in ys]
        pts = list(zip(xs, ys))

    return pts

pts = []
for d in dat:
    if "," in d:
        x, y = d.split(",")
        pts.append((int(x), int(y)))
    elif "fold" in d:
        print(d)
        f = d.split(" ")[-1]
        axis, dist = f.split("=")
        dist = int(dist)
        pts = do_fold(pts, axis, dist)
        break
    else:
        pass
print(len(set(pts)))
