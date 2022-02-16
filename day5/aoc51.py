#!/usr/bin/env python3

import numpy as np


fname = "input.txt"
with open(fname) as f:
    data = f.readlines()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.xmin = min(self.p1.x, self.p2.x)
        self.xmax = max(self.p1.x, self.p2.x)
        self.ymin = min(self.p1.y, self.p2.y)
        self.ymax = max(self.p1.y, self.p2.y)
    
        self.horiz = self.is_horiz()
        self.vert = self.is_vert()

        self.pts = set()

        if self.horiz:
            for i in range(self.xmin, self.xmax+1):
                self.pts.add(Point(i, self.ymin))
        elif self.vert:
            for i in range(self.ymin, self.ymax+1):
                self.pts.add(Point(self.xmin, i))
        else:  # non-horiz/vert
            pass

    def is_horiz(self):
        if self.p1.y == self.p2.y:
            return True
        else:
            return False

    def is_vert(self):
        if self.p1.x == self.p2.x:
            return True
        else:
            return False

    def intersect(self, ls):
        return self.pts.intersection(ls.pts)

    def contains(self, p):
        return p in self.pts

    def __repr__(self):
        if not self.pts:
            print("non horiz/vert: ", self.p1, self.p2)
        else:            
            for p in self.pts:
                print(p)
        return ""
        
data = [x.strip().split(" -> ") for x in data]
        
def get_point(s):
    r = s.split(",")
    return Point(int(r[0]), int(r[1]))

data = [list(map(get_point, x)) for x in data]
data = [LineSegment(x[0], x[1]) for x in data]

rel = [x for x in data if x.horiz or x.vert]

# all the coords are non-negative
xmax = max([seg.xmax for seg in rel])
ymax = max([seg.ymax for seg in rel])
arr = np.zeros((xmax + 1, ymax + 1))

for seg in rel:
    for p in seg.pts:
        arr[p.x, p.y] += 1

ctr = 0
for x in range(xmax +1):
    for y in range(ymax +1):
        if arr[x, y] > 1:
            ctr += 1
print(ctr)
