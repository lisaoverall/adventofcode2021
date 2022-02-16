#!/usr/bin/env python3

from collections import Counter

fname = "input.txt"
NUM_STEPS = 10
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

template = dat[0]
rule = [d.split(" -> ") for d in dat[2:]]
rule = {p: i for p, i in rule}

def pairs(s):
    return [s[i:i+2] for i in range(len(s)-1)]

def step(s, rs):
    ps = pairs(s)
    return "".join([p[0] + rs[p] for p in ps]) + s[-1]

for _ in range(1, NUM_STEPS+1):
    template = step(template, rule)

cts = Counter(template).most_common()
most = cts[0][1]
least = cts[-1][1]
print(most - least)

