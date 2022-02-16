#!/usr/bin/env python3

fname = "input.txt"
NUM_DAYS = 256

with open(fname) as f:
    dat = [int (x) for x in f.readline().strip().split(",")]

fish = [0]*9
for i in range(len(fish)):
    fish[i] = dat.count(i)

for i in range(NUM_DAYS):
    z = fish[0]
    for i in range(len(fish) - 1):
        fish[i] = fish[i+1]
    fish[6] += z
    fish[8] = z

print(sum(fish))
