#!/usr/bin/env python3

fname = "input.txt"
nsteps = 100
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False

    def __repr__(self):
        return str(self.energy) 

    def flash(self):
        self.flashed = True
        self.energy = 0

    def inc(self):
        self.energy += 1

    def reset(self):
        self.flashed = False

dat = [list(map(lambda y: Octopus(int(y)), iter(x))) for x in dat]
for d in dat:
    print(d)
print("-------------------")

ymax = len(dat) - 1
xmax = len(dat[0]) - 1

def neighbors(y, x):
    if y == 0:
        if x == 0:
            return [(0, 1), (1, 0), (1, 1)]
        elif x == xmax:
            return [(0, xmax-1), (1, xmax), (1, xmax-1)]
        else:
            return [(0, x-1), (0, x+1), (1, x-1), (1, x), (1, x+1)]
    elif y == ymax:
        if x == 0:
            return [(ymax, 1), (ymax-1, 0), (ymax-1, 1)]
        elif x == xmax:
            return [(ymax, xmax-1), (ymax-1, xmax), (ymax-1, xmax-1)]
        else:
            return [(ymax, x-1), (ymax, x+1), (ymax-1, x-1), (ymax-1, x), (ymax-1, x+1)]
    else:
        if x == 0:
            return [(y-1, 0), (y+1, 0), (y-1, 1), (y, 1), (y+1, 1)]
        elif x == xmax:
            return [(y-1, xmax), (y+1, xmax), (y-1, xmax-1), (y, xmax-1), (y+1, xmax-1)]
        else:
            return [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]


def step():

    ready = [] 
    for y in range(ymax+1):
        for x in range(xmax+1):
            octo = dat[y][x]
            octo.inc()
            if octo.energy > 9:
                ready.append((y, x))
    
    while ready:
        flashed = []
        for (i, j) in ready:
            dat[i][j].flash()
            flashed.append((i,j))

        ready = []

        for (i, j) in flashed:
            ns = neighbors(i, j)
            for (y, x) in ns:
                n = dat[y][x]
                if not n.flashed:
                    n.inc()

        for y in range(ymax+1):
            for x in range(xmax+1):
                if dat[y][x].energy > 9:
                    ready.append((y, x))

    ctr = 0
    for y in range(ymax+1):
        for x in range(xmax+1):
            octo = dat[y][x]
            if octo.flashed:
                ctr += 1
                octo.reset()

    return ctr

total = 0
for i in range(1, nsteps+1):
    total += step()
    # print("step", i)
    # for d in dat:
    #     print(d)

    # print ("------------")

print(total)
