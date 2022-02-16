#!/usr/bin/env python3

fname = "input.txt"
with open(fname) as f:
    dat = [int(x) for x in f.read().strip().split(",")]

def cost(start, end):
    dist = abs(start - end)
    return sum(range(1, dist + 1))

best = 1000000000
for i in range(min(dat), max(dat) + 1):
    res = sum([cost(x, i) for x in dat])
    if res < best:
        best = res
print(best)


