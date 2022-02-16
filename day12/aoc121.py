#!/usr/bin/env python3

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

paths = []
def walk(node, visited):
    visited.append(node)
    for neighbor in graph[node]:
        if is_cave_big(neighbor) or neighbor not in visited:
            walk(neighbor, visited.copy())
    paths.append(visited)

walk("start", [])
valid = [p for p in paths if p[-1] == 'end']
print(valid)
print(len(valid))
