#!/usr/bin/env python3

fname = "input.txt"
with open(fname) as f:
    dat = f.readlines()

dat = [x.strip().split(" | ") for x in dat]
inputs = [x[0].split() for x in dat]
outputs = [x[1].split() for x in dat] 

segs = ['abcefg',   # 0
        'cf',       # 1
        'acdeg',    # 2
        'acdfg',    # 3
        'bcdf',     # 4
        'abdfg',    # 5
        'abdefg',   # 6
        'acf',      # 7 
        'abcdefg',  # 8
        'abcdfg'    # 9
       ]

def segcount_to_wires(x):
    d = {i: [] for i in range(10)}
    for y in x:
        d[len(y)].append(y)
    return d


def segments_to_wires(x):
    
    cs = segcount_to_wires(x)  # k, v = wirecount, set(str)

    m = {k: None for k in 'abcdefg'}  # k, v = segment, wire
    
    n = {i: None for i in range(10)}  # k, v = number, wires
    for i in [1, 4, 7, 8]:
        n[i] = set(cs[len(segs[i])][0])
   
    m['a'] = next(iter(n[7] - n[1]))

    # 6x segments - 0, 6, 9
    # identify 6 by unioning with 1 and seeing if you get 8
    for i in cs[6]:
        if set(i).union(n[1]) == n[8]:
            n[6] = set(i)
            m['c'] = next(iter(n[1] - n[6]))

    m['f'] = next(iter(n[1] - set(m['c'])))

    # 5x segments - 2, 3, 5
    for i in cs[5]:
        if m['c'] not in i:
            n[5] = set(i)
        else:
            if m['f'] in i:
                n[3] = set(i)
            else:
                n[2] = set(i)

    m['e'] = next(iter(n[6] - n[5]))

    # distinguish between 0 and 9
    for i in cs[6]:
        if set(i) != n[6]:
            if m['e'] in i:
                n[0] = set(i)
            else:
                n[9] = set(i)

    # invert dictionary: k, v =  (alphabetized) segs as strings, number
    return {"".join(sorted(v)): k for (k, v) in n.items()}


def decode_digit(x, d):
    return d["".join(sorted(x))]

def decode_row(j, d):
    lenj = len(j)
    ctr = sum([decode_digit(j[i], d) * 10**(lenj-1-i) for i in range(lenj)])

    # res = int("".join([str(decode_digit(x, d)) for x in j]))
    # assert(ctr == res)
    
    return ctr

ds = [segments_to_wires(i) for i in inputs]
decodes = [decode_row(j, d) for j, d in zip(outputs, ds)]
print(sum(decodes))
