#!/usr/bin/env python3
# https://adventofcode.com/2021/day/12

from collections import Counter, defaultdict


def walk(c, visited, allowed):
    global paths

    if c.islower():
        visited[c] += 1
    if allowed:
        if 2 in visited.values():
            allowed = False
    for p in connected[c]:
        if p.isupper() or (visited[p] < 1 or allowed) and p != 'start':
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
walk('start', Counter(), False)
print('p1 =', paths)

paths = 0
walk('start', Counter(), True)
print('p2 =', paths)

