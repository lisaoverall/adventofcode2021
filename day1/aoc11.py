#!/usr/bin/env python3

# How many measurements are larger than the previous measurement?

with open("input.txt") as f:
    data = f.readlines()

data = [int(x.strip()) for x in data]
print(data)

count = 0
tmp = data[0]

for i in data:
    if i > tmp:
        count += 1
    tmp = i

print(count)
