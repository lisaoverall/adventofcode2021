#!/usr/bin/env python3

from collections import deque

fname = "input.txt"
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

pts = {')': 1, ']': 2, '}': 3, '>': 4}

def score(cstr, pts):
    s = 0
    for c in cstr:
        s *= 5
        s += pts[c]
    return s

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
                return ''
    
    if len(d):
        return fix_incomplete(d)
    else:
        return ''

def fix_incomplete(d):
    m = {'(': ')', '[': ']', '{': '}', '<': '>'}
    res = ''
    for _ in range(len(d)):
        c = d.pop()
        res += m[c]
    return res

res = sorted(filter(lambda x: x > 0, 
        map(lambda x: score(x, pts), map(process_line, dat))))
print(res[len(res)//2])

