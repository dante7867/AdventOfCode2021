#!/usr/bin/env python3
# https://adventofcode.com/2021/day/1

def p1(x):
    c = 0
    for d1, d2 in zip(d, d[x:]):
        if d2>d1:
            c += 1
    return c 


if __name__ == "__main__":
    with open('i.txt', 'r') as file:
        d = [int(line) for line in file.readlines()]
    print(f"p1 = {p1(1)}")
    print(f"p2 = {p1(3)}")
