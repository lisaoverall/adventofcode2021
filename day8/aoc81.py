#!/usr/bin/env python3

fname = "input.txt"
with open(fname) as f:
    dat = f.readlines()

dat = [x.strip().split(" | ") for x in dat]
inputs = [x[0].split() for x in dat]
outputs = [x[1].split() for x in dat] 

segs = ['abcefg',   # 0
        'cf',       # 1
        'acdeg',    # 2
        'acdfg',    # 3
        'bcdf',     # 4
        'abdfg',    # 5
        'abdefg',   # 6
        'acf',      # 7 
        'abcdefg',  # 8
        'abcdfg'    # 9
       ]

easy_lens = set(len(x) for x in [segs[1], segs[4], segs[7], segs[8]])

ctr = 0
for x in outputs:
    ctr += sum([len(y) in easy_lens for y in x])
print(ctr)
