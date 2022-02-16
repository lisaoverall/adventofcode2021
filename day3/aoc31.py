#!/usr/bin/env python3

from collections import Counter

fname = "input.txt"
with open(fname) as f:
    data = f.readlines()

data = [x.strip() for x in data]

def most(lst):
    return Counter(lst).most_common(1)[0][0]

def least(lst):
    return Counter(lst).most_common()[-1][0][0]

def f(dat, fltr):
    res = ''
    for i in range(len(dat[0])):
        d = [x[i] for x in dat]
        res += fltr(d)
    return res

def gamma_rate(d):
    return f(d, most)

def epsilon_rate(d):
    return f(d, least)

print(int(gamma_rate(data), base=2) * int(epsilon_rate(data), base=2))
