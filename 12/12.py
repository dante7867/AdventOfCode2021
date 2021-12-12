#!/usr/bin/env python3
# https://adventofcode.com/2021/day/12

from collections import Counter, defaultdict


def walk(c, visited, allowed):
    global paths

    if c.islower():
        visited.append(c)
        if visited.count(c) == 2:
            allowed = False
    for p in connected[c]:
        if p.isupper() or (allowed or p not in visited) and p != 'start':
            if p == 'end':
                paths += 1
            else: 
                walk(p, visited.copy(), allowed)


connected = defaultdict(set)
with open('i.txt','r') as f:
    for line in f.readlines():
        line = line.strip().split('-')
        connected[line[0]].add(line[1])
        connected[line[1]].add(line[0])

paths = 0
walk('start', [], False)
print('p1 =', paths)

paths = 0
walk('start', [], True)
print('p2 =', paths)

