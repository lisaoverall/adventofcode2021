#!/usr/bin/env python3

from collections import Counter

fname = "input.txt"
with open(fname) as f:
    dat = [x.strip() for x in f.readlines()]

graph = {}
for d in dat:
    n1, n2 = d.split('-')
    graph.setdefault(n1, []).append(n2)
    graph.setdefault(n2, []).append(n1)

def is_cave_big(n):
    if n.isupper():
        return True
    else:
        return False

def middle(n):
    return n not in set(["start", "end"])

paths = []
def walk(node, visited):
    visited.append(node)
    toomany = {n: c for n, c in Counter(visited).items() \
            if not is_cave_big(n) and middle(n) and c > 1}
    for neighbor in graph[node]:
        if is_cave_big(neighbor) or \
                (middle(neighbor) and len(toomany.keys()) == 0) or \
                neighbor not in visited:
            walk(neighbor, visited.copy())
    paths.append(visited)

walk("start", [])
valid = [p for p in paths if p[-1] == 'end']
print(valid)
print(len(valid))
