#!/usr/bin/env python3
# https://adventofcode.com/2021/day/13


def count_dots(paper):
    dots_count = 0
    for row in paper:
        for val in row:
            if val:
                dots_count += 1 
    return dots_count


def print_paper(paper):
    for row in paper:
        s = ""
        for val in row:
            if val:
                s += '#'
            else:
                s += '.'
        print(s)


def fold_y(paper, fold_y_axis):
    up, down = paper[:fold_y_axis], paper[fold_y_axis+1:]

    if len(up) > len(down):
        while len(down) != len(up):
            down.append([False]*len(down[0]))
    else:
        while len(down) != len(up):
            up = [[False]*len(down[0])] + up
    down = down[::-1]
    for y in range(len(up)):
        for x in range(len(up[0])):
            up[y][x] += down[y][x]

    return up 
    
    
def fold_x(paper, fold_x_axis):
    left, right = [], []

    for row in paper:
        left.append(row[:fold_x_axis])
        right.append(row[fold_x_axis+1:][::-1])
    
    if len(left[0]) > len(right[0]):
        for row in right:
            while len(row) != len(left[0]):
                row = [False] + row
    else:
        for row in left:
            while len(row) != len(right[0]):
                row = [False] + row

    for y in range(len(left)):
        for x in range(len(left[0])):
            left[y][x] += right[y][x]

    return left 


with open('i.txt','r') as f:
    dots = []
    folds = []
    read_dots = True
    for line in f.readlines():
        if line == '\n':
            read_dots = False
            continue
        if read_dots:
            line = line.strip().split(',')
            dots.append( tuple([int(num) for num in line]) )
        else: # read folds
            line = line.strip().split(' ')
            fold = line[2].split('=')
            folds.append((fold[0], int(fold[1]), ))

    x_max, y_max = 0,0
    for point in dots:
        x, y = point
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
    paper = []
    for _ in range(y_max+1):
        paper.append([False]*(x_max+1))

    for point in dots:
        x, y = point
        paper[y][x] = True
    
    for fold in folds:
        if fold[0] == 'x':
            paper = fold_x(paper, fold[1])
        if fold[0] == 'y':
            paper = fold_y(paper, fold[1])
    print_paper(paper)

