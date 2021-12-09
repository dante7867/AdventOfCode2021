#!/usr/bin/env python3
# https://adventofcode.com/2021/day/9


def p1():
    risk_level = 0
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if x-1>-1:
                if mapa[y][x] >= mapa[y][x-1]:
                    continue
            if x+1 < len(mapa[0]):
                if mapa[y][x] >= mapa[y][x+1]:
                    continue
            if y-1>-1:
                if mapa[y][x] >= mapa[y-1][x]:
                    continue
            if y+1<len(mapa):
                if mapa[y][x] >= mapa[y+1][x]:
                    continue
            risk_level += mapa[y][x] + 1
            lowests.append((y,x))
    return risk_level, lowests


def get_basin_size(y,x):
    basin = set()
    basin.add((y,x))

    if x-1>-1:
        if mapa[y][x] < mapa[y][x-1] and mapa[y][x-1] != 9:
            basin |= get_basin_size(y,x-1)
    if x+1 < len(mapa[0]):
        if mapa[y][x] < mapa[y][x+1] and mapa[y][x+1] != 9:
            basin |= get_basin_size(y,x+1)
    if y-1>-1:
        if mapa[y][x] < mapa[y-1][x] and mapa[y-1][x] != 9:
            basin |= get_basin_size(y-1,x)
    if y+1<len(mapa):
        if mapa[y][x] < mapa[y+1][x] and mapa[y+1][x] != 9:
            basin |= get_basin_size(y+1,x)
    return basin


def p2(lowests):
    basins = []
    for l in lowests:
        y, x = l
        basins.append(len(get_basin_size(y,x)))
    basins = sorted(basins)
    print('p2 = ',basins[-1]*basins[-2]*basins[-3])


global mapa
lowests = []
if __name__ == "__main__":
    with open('i.txt','r') as f:
        mapa = [list(row.strip()) for row in f.readlines()]
        for idx,row in enumerate(mapa):
            mapa[idx] = [int(x) for x in row]
    
    risk_level, lowests = p1()
    print("p1 = ", risk_level)

    p2(lowests)
    
