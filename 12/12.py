from collections import Counter
from copy import deepcopy


connected = {}
with open('i.txt','r') as f:
    for line in f.readlines():
        line = line.strip().split('-')
        if line[0] not in connected:
            connected[line[0]] = set([line[1]])
        else:
            connected[line[0]].add(line[1])
        if line[1] not in connected:
            connected[line[1]] = set([line[0]])
        else:
            connected[line[1]].add(line[0])


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

paths = set()
walk('start', 'start', Counter(), False)
print(f'p1 = {len(paths)}')

walk('start', 'start', Counter(), True)
print(f'p2 = {len(paths)}')

