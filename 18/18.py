#!/usr/bin/env python3
# https://adventofcode.com/2021/day/18
import math 


def explode(n, i): 
    for j in range(i, 0, -1):
        if type(n[j]) is int:
            n[j] += n[i + 1]
            break

    for j in range(i+4, len(n)):
        if type(n[j]) is int:
            n[j] += n[i + 3]
            break

    n[i] = 0
    for x in range(1,5):
        n[i+x] = ''
   
    n = [x for x in n if x != '']
    return n


def split(n):
    new_list = []
    nothing_splitted = True

    for i in range(len(n)):
        if nothing_splitted and type(n[i]) is int and n[i] > 9:
            new_list.append('[')
            new_list.append( int(math.floor( n[i]/2 )) )
            new_list.append(',')
            new_list.append( int(math.ceil( n[i]/2 )) )
            new_list.append(']')
            nothing_splitted = False
        else:
            new_list.append(n[i])
    return new_list


def snailfish_sum(l1, l2):
    return ['['] + l1 + [','] + l2 + [']']


def reduce(n):
    nest = 0

    action = False
    for i in range(len(n)):
        if n[i] == '[':
            nest += 1
        elif n[i] == ']':
            nest -= 1

        if nest == 5:
            n = explode(n, i)
            action = True
            break
    if not action:
        for i in range(len(n)):
            if type(n[i]) is int and n[i] > 9:
                n = split(n)
                break
    return n


def keep_reducing(n):
    while True:
        cp = n.copy()
        n = reduce(n)
        if n == cp:
            break
    return n


def calculate_magnitude(n):
    while len(n) != 1:
        for i in range(len(n)):
            if n[i] == '[' and n[i+4] == ']':
                n[i] = 3 * n[i+1] + 2 * n[i+3]
                for j in range(1,5):
                    n[i+j] =''
        n = [x for x in n if x != '']
    return n[0]


def p1(lines):
    current = lines[0]
    for i in range(1, len(lines)):
        current = snailfish_sum(current, lines[i])
        current = keep_reducing(current)
    return calculate_magnitude(current) 


def p2(lines):
    max_magni = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                current = snailfish_sum(lines[i], lines[j])
                current = keep_reducing(current)
                magni = calculate_magnitude(current)
                max_magni = max(max_magni, magni)
    return max_magni

if __name__ == "__main__":
    with open('i.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    for i,s in enumerate(lines):
        lines[i] = [int(x) if x.isdigit() else x for x in s]

    print(f'p1 = {p1(lines.copy())}')
    print(f'p2 = {p2(lines.copy())}')
