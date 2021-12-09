#!/usr/bin/env python3
# https://adventofcode.com/2021/day/5
from collections import Counter
from copy import deepcopy

def fishes_at_day(fishes, days):
    for d in range(days):
        fishes[(d+7)%9] += fishes[d%9]
    return sum(fishes.values())

if __name__ == "__main__":
    with open('i.txt', 'r') as f:
        fishes = Counter([int(x) for x in f.readline().strip().split(',')])
    
    print('p1 = ',fishes_at_day(deepcopy(fishes), 80))
    print('p2 = ',fishes_at_day(fishes, 256))

