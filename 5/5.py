#!/usr/bin/env python3
# https://adventofcode.com/2021/day/5
from math import gcd

def draw_line(line, map, consider_diagonals):
    i = line[2] - line[0]
    j = line[3] - line[1]

    ux = int(i / gcd(i, j))
    uy = int(j /gcd(i, j))

    if ux == 0 or uy == 0 or consider_diagonals:
        x = line[0]
        y = line[1]
        map[y][x] += 1
        while not (x == line[2] and y == line[3]):
            x += ux
            y += uy 
            map[y][x] += 1


def get_number_of_overlapping_fields(map):
    overlapping = 0
    for row in map:
        for n in row:
            if n > 1:
                overlapping += 1
    return overlapping


def p1():
    map = [[0] * (size + 1) for _ in range(size + 1)]
    for pair in pairs:
        draw_line(pair, map, False)
    return get_number_of_overlapping_fields(map)


def p2():
    map = [[0] * (size + 1) for _ in range(size + 1)]
    for pair in pairs:
        draw_line(pair, map, True)
    return get_number_of_overlapping_fields(map)


if __name__ == "__main__":
    with open('i.txt', 'r') as f:
        pairs = []
        for line in f.readlines():
            pairs.append([int(x) for x in line.strip().replace('-', ',').replace('>', '').replace(' ', '').split(',')])

    size = 0
    for pair in pairs:
        if max(pair) > size:
            size = max(pair)

    print(f"{p1() = }")
    print(f"{p2() = }")

