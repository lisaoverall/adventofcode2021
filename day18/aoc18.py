#!/usr/bin/env python3

import json

fname = "input.txt"
with open(fname) as f:
    dat = [json.loads(x) for x in f.readlines()]


class SnailNum:
    def __init__(self, parent, depth):
        self.parent = parent
        self.depth = depth

    def __add__(self, other):
        assert(isinstance(other, SnailNum) and self.depth == other.depth == 0)
        pair = Pair(self.copy(), other.copy(), None, -1)
        pair.l.parent = pair.r.parent = pair
        for e in pair.walk():
            e.depth += 1
        pair.reduce()
        return pair

    def _reduce(self):
        for e in self.walk():
            if (isinstance(e, Pair) and e.depth >= 4 and \
                    isinstance(e.l, Num) and isinstance(e.r, Num)):
                e.explode()
                return True
        for e in self.walk():
            if isinstance(e, Num) and e.value >= 10:
                e.split()
                return True
        return False

    def reduce(self):
        while self._reduce():
            pass


class Pair(SnailNum):
    def __init__(self, l, r, parent, depth):
        super().__init__(parent, depth)
        self.l = l
        self.r = r

    def __repr__(self):
        return repr([self.l, self.r])

    def magnitude(self):
        return 3*self.l.magnitude() + 2*self.r.magnitude()

    def copy(self, parent=None):
        p = Pair(None, None, parent, self.depth)
        p.l = self.l.copy(parent=p)
        p.r = self.r.copy(parent=p)
        return p

    def walk(self, reverse=False):
        first, second = (self.r, self.l) if reverse else (self.l, self.r)
        yield from first.walk(reverse)
        yield self
        yield from second.walk(reverse)

    def next_number(self, reverse=False):
        if not self.parent:
            return None
        sibling = self.parent.l if reverse else self.parent.r
        if self is sibling:
            return self.parent.next_number(reverse)
        for e in sibling.walk(reverse=reverse):
            if isinstance(e, Num):
                return e
        assert 0, "unreachable"

    def explode(self):
        l = self.next_number(reverse=True)
        if l:
            l.value += self.l.value
        r = self.next_number(reverse=False)
        if r:
            r.value += self.r.value
        if self is self.parent.l:
            self.parent.l = Num(0, parent=self.parent, depth=self.depth)
        else:
            self.parent.r = Num(0, parent=self.parent, depth=self.depth)


class Num(SnailNum):
    def __init__(self, value, parent, depth):
        super().__init__(parent, depth)
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def magnitude(self):
        return self.value

    def copy(self, parent=None):
        return Num(self.value, parent, self.depth)

    def walk(self, reverse=False):
        yield self

    def split(self):
        pair = Pair(None, None, parent=self.parent, depth=self.depth)
        pair.l = Num(self.value // 2, parent=pair, depth=pair.depth+1)
        pair.r = Num(self.value - pair.l.value, parent=pair, depth=pair.depth+1)
        if self is self.parent.l:
            self.parent.l = pair
        else:
            self.parent.r = pair
    
    
def parse_expr(expr, parent=None, depth=0):
    if isinstance(expr, int):
        return Num(expr, parent, depth)
    assert(isinstance(expr, list) and len(expr) == 2)
    pair = Pair(None, None, parent, depth)
    pair.l = parse_expr(expr[0], parent=pair, depth=depth+1)
    pair.r = parse_expr(expr[1], parent=pair, depth=depth+1)
    return pair

sns = [parse_expr(x) for x in dat]
print(sum(sns[1:], sns[0]).magnitude())  # part 1

magnitude = 0
for a in sns:
    for b in sns:
        if a is not b:
            magnitude = max(magnitude, (a+b).magnitude())
print(magnitude)  # part 2
