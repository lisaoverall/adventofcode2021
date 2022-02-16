#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.readlines()

data = [int(x.strip()) for x in data]

count = 0

for i in range(1, len(data)-2):
    tmp0 = sum(data[i-1:i+2])
    tmp1 = sum(data[i:i+3])
    # print(tmp0, tmp1)
    if tmp0 < tmp1:
        count += 1

print(count)
