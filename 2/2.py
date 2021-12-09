#!/usr/bin/env python3
# https://adventofcode.com/2021/day/2


def p1():
    front, depth = 0, 0
    for i in ins:
        if i[0] == 'forward':
            front += int(i[1])
        if i[0] == 'down':
            depth += int(i[1])
        if i[0] == 'up':
            depth -= int(i[1])
    return depth * front


def p2():
    front, depth, aim = 0, 0, 0
    for i in ins:
        if i[0] == 'forward':

            front += int(i[1])
            depth += aim*int(i[1])
        if i[0] == 'down':
            aim += int(i[1])
        if i[0] == 'up':
            aim -= int(i[1])
    return depth * front


if __name__ == "__main__":
    with open('i.txt', 'r') as file:
        ins = [line.strip().split(' ') for line in file.readlines()]
    print(f'{p1() = }')
    print(f'{p2() = }')

