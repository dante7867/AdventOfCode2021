#!/usr/bin/env python3
# https://adventofcode.com/2021/day/15
from queue import PriorityQueue
import sys
sys.path.append("..")
from timing import timer


def estabish_costs(points,cave,end):
    risks = []
    for _ in range(len(cave)):
        risks.append( [1e9]*len(cave[0]) )

    while not points.empty():
        risk, (y,x) = points.get()
        for j, i in [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]:
            if i > -1 and i < len(cave[0]) and j > -1 and j < len(cave):
                if risk + cave[j][i] < risks[j][i]:
                    risks[j][i] = risk+cave[j][i]
                    pt = (risks[j][i], (j, i))
                    points.put(pt)
                    if (j, i) == end:
                        return risks[j][i]


def increment_or_wrap(x, val):
    for _ in range(val):
        x = x + 1
        if x == 10:
            x = 1
    return x


def get_new_cave(cave):
    # scale horizontally
    new_cave = []
    for x in range(len(cave)):
        new_cave.append([])
        for y in range(5):
            new_cave[x] += [increment_or_wrap(x,y) for x in cave[x]]
    # scale vertically
    for a in range(4):
        for r in range(len(cave)):
            new_cave.append([increment_or_wrap(x,a+1) for x in new_cave[r]])
    return new_cave


@timer
def p1():
    y, x = 0, 0
    (y_end, x_end) = len(cave) - 1, len(cave[0]) - 1

    points = PriorityQueue()
    points.put((0,(y,x)))

    return estabish_costs(points, cave, (y_end, x_end))


@timer
def p2():
    new_cave = get_new_cave(cave)
    y, x = 0, 0
    (y_end, x_end) = len(new_cave) - 1, len(new_cave[0]) - 1

    points = PriorityQueue()
    points.put((0,(y,x)))
    
    return estabish_costs(points, new_cave, (y_end, x_end))


if __name__ == "__main__":
    cave = []
    with open('i.txt','r') as f:
        for line in f.readlines():
            line = line.strip()
            cave.append([int(x) for x in line])

    print(f'{p1() = }')
    print(f'{p2() = }')
