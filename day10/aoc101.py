#!/usr/bin/env python3

from collections import deque

fname = "input.txt"
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

pts = {')': 3, ']': 57, '}': 1197, '>' :25137}
count = {k: 0 for k in ")]}>"}

def score(count, pts):
    return sum([pts[k]*v for (k, v) in count.items()])

def match(c, i):
    return (c, i) in set([('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')])

def process_line(x):
    d = deque()
    for i in x:
        if i in "([{<":
            d.append(i)
        else:
            c = d.pop()
            if match(c, i):
                pass
            else:  # corrupted line
                count[i] += 1
                break

for d in dat:
    process_line(d)
print(score(count, pts))

