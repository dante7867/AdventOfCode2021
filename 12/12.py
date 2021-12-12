#!/usr/bin/env python3
# https://adventofcode.com/2021/day/12

from collections import Counter, defaultdict
from copy import deepcopy


def walk(c, h, visited, allowed):
    if c.islower():
        visited[c] += 1
    if allowed:
        if 2 in visited.values():
            allowed = False
    for p in connected[c]:
        if p.isupper() or (p.islower() and (visited[p] < 1 or allowed)) and p != 'start':
            if p == 'end':
                paths.add(h + ',' + p)
            else: 
                walk(p, h + ',' + p,deepcopy(visited), deepcopy(allowed))


connected = defaultdict(set)
with open('i.txt','r') as f:
    for line in f.readlines():
        line = line.strip().split('-')
        connected[line[0]].add(line[1])
        connected[line[1]].add(line[0])

paths = set()

walk('start', 'start', Counter(), False)
print(f'p1 = {len(paths)}')

walk('start', 'start', Counter(), True)
print(f'p2 = {len(paths)}')

