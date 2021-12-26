#!/usr/bin/env python3
# https://adventofcode.com/2021/day/25


def print_seafloor(seafloor):
    print('-'*10)
    for row in seafloor:
        print(''.join(row))
    print('-'*10)


def move_east(old):
    new = []

    for y in range(len(old)):
        new_row = ['.']*len(old[0])
        
        for x in range(len(old[0])):
            if old[y][x] == '>':
                target = x + 1
                if target == len(old[0]):
                    target = 0

                if old[y][target] == '.':
                    new_row[target] = '>'
                else:
                    new_row[x] = '>'

        new.append(new_row)

    return new


def move_south(old, after_east):
    new = after_east.copy()

    for y in range(len(old)):
        for x in range(len(old[0])):
            if old[y][x] == 'v':

                target = y + 1
                if target == len(old):
                    target = 0

                if after_east[target][x] == '.' and old[target][x] != 'v':
                    new[target][x] = 'v'
                else:
                    new[y][x] = 'v'
    return new



def step(old):
    after_east = move_east(old)
    new = move_south(old, after_east)
    if new == old:
        return new, True
    return new, False 
    

with open('i.txt', 'r') as f:
    seafloor = [list(line.strip()) for line in f.readlines()]
    
stop = False
step_number = 0
while not stop:
    step_number += 1
    seafloor, stop = step(seafloor)
    # print(f'After {step_number} steps')
    # print_seafloor(seafloor)

print('p1', step_number)

