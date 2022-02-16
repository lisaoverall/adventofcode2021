#!/usr/bin/env python3

from collections import Counter

fname = "input.txt"
NUM_STEPS = 40
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

template = dat[0]
rule = [d.split(" -> ") for d in dat[2:]]
rule = {p: i for p, i in rule}

def pairs(s):
    return [s[i:i+2] for i in range(len(s)-1)]

def step(s, rs, nsteps):
    elt_cts = Counter(s)
    pair_cts = Counter(pairs(s))
    for _ in range(nsteps):
        new_pair_cts = Counter()
        for p, n in pair_cts.items():
            i = rs[p]
            new_pair_cts[p[0] + i] += n
            new_pair_cts[i + p[1]] += n
            elt_cts[i] += n
        pair_cts = new_pair_cts
    return elt_cts

cts = step(template, rule, NUM_STEPS).most_common()
most = cts[0][1]
least = cts[-1][1]
print(most - least)

