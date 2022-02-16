#!/usr/bin/env python3

fname = "input.txt"
with open(fname) as f:
    dat = f.readlines()

def is_low_point(c, up, down, left, right):
    return all([c < x for x in [up, down, left, right]])

def risk_level(p):
    return 1 + p

dat = [list(map(int, list(d.strip()))) for d in dat]

maxx = len(dat[0])
maxy = len(dat)

ctr = 0
for i in range(maxy):
    for j in range(maxx):
        if i == 0:
            up = 100
            down = dat[i+1][j]
        elif i == maxy - 1:
            up = dat[i-1][j]
            down = 100
        else:
            up = dat[i-1][j]
            down = dat[i+1][j]

        if j == 0:
            left = 100
            right = dat[i][j+1]
        elif j == maxx - 1:
            left = dat[i][j-1]
            right = 100
        else:
            left = dat[i][j-1]
            right= dat[i][j+1]

        p = dat[i][j]
        if is_low_point(p, up, down, left, right):
            ctr += risk_level(p)

print(ctr)
