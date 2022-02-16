#!/usr/bin/env python3

fname = "input.txt"
with open(fname) as f:
    dat = f.read().split()
xmin, xmax = [int(x) for x in dat[2][2:-1].split("..")]
ymin, ymax = [int(y) for y in dat[3][2:].split("..")]

x0, y0 = 0, 0

# Part 1: what is max height projectile can reach?
vy_max = abs(ymin + 1)  
max_height = (vy_max + 1) * vy_max/2
print(max_height)

def xs(v, p=0):
    while p <= xmax:
        yield p >= xmin 
        p += v
        v -= (v > 0)

def ys(v, p=0):
    while p >= ymin:
        yield p <= ymax
        p += v
        v -= 1


hits_target = sum(any(map(lambda a,b: a&b, xs(x), ys(y)))
    for x in range(1+xmax) for y in range(ymin,-ymin))
print(hits_target)



