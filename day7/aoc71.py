#!/usr/bin/env python3

fname = "input.txt"
with open(fname) as f:
    dat = [int(x) for x in f.read().strip().split(",")]

best = 1000000
for i in range(min(dat), max(dat) + 1):
    res = sum([abs(x - i) for x in dat])
    if res < best:
        best = res
print(best)


