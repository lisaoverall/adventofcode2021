#!/usr/bin/env python3

from collections import Counter

fname = "input.txt"
with open(fname) as f:
    data = f.readlines()

data = [x.strip() for x in data]

def rate(dat, pref):

    if pref == '0':
        nonpref = '1'
    else:  # pref == '1'
        nonpref = '0'

    res = dat
    for i in range(len(dat[0])):
        d = [x[i] for x in res]
        c = Counter(d)
        zeros = c['0']
        ones = c['1']
        if zeros > ones:
            res = list(filter(lambda x: x[i] == nonpref, res))
        else:
            res = list(filter(lambda x: x[i] == pref, res))
        if len(res) == 1:
            res = res[0]
            break
    return res

def ox_rate(dat):
    return rate(dat, '1')

def co2_rate(dat):
    return rate(dat, '0')

def life_support(dat):
    return int(ox_rate(dat), base=2) * int(co2_rate(data), base=2)

print(life_support(data))
