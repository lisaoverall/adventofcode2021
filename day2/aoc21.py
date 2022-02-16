#!/usr/bin/env python3

fname = "input.txt" 
with open(fname) as f:
    data = f.readlines()

data = [x.split() for x in data]
data = [(x, int(y)) for (x, y) in data] 

horiz = 0
depth = 0

for i in data:
    direction = i[0]
    val = i[1]
    if direction == "forward":
        horiz += val
    elif direction == "up":
        depth  -= val
    else:  # direction == "down"
        depth += val

print(horiz*depth)
