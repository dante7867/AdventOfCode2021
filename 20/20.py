#!/usr/bin/env python3
# https://adventofcode.com/2021/day/20
import sys
sys.path.append('..')
from timing import timer


def extend_image(image, n):
    NEW_SIZE = len(image) + 2 * n
    extended = []
    for _ in range(n):
        extended.append(['.']*NEW_SIZE)

    for i in range(len(image)):
        extended.append(['.']*n + image[i] + ['.']*n)

    for _ in range(n):
        extended.append(['.']*NEW_SIZE) 
    
    return extended


def create_blank_image(SIZE):
    new_image = []
    for _ in range(SIZE):
        new_image.append(['.']*SIZE)
    return new_image


def enhance_pixel(image, y, x):
    frame = ""
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if x+dx >-1 and x+dx <len(image[0]) and y+dy > -1 and y+dy<len(image):
                if image[y+dy][x+dx] == '#':
                    frame += '1'
                else:
                    frame += '0'
            else:
                frame += '0'
    decimal = int(frame,2)
    return algo[decimal]


def print_img(image):
    print()
    for row in image:
        print(''.join(row))
    print()


def enhance_image(image, algo):
    SIZE = len(image)
    enhanced = create_blank_image(SIZE)
    for y in range(SIZE):
        for x in range(SIZE):
            enhanced[y][x] = enhance_pixel(image, y, x)

    return enhanced


def enhance_n_steps(image, algo, steps):
    for x in range(steps):
        image = enhance_image(image, algo)
    return image


def eval_image(image):
    bright_pixels_cnt = 0
    for row in image:
        for pixel in row:
            if pixel == '#':
                bright_pixels_cnt += 1

    return bright_pixels_cnt


@timer
def count_lighs_on(image, steps):
    image = extend_image(image,steps*2)

    image = enhance_n_steps(image, algo, steps)
    cnt = 0
    for i in range(steps,len(image)-steps):
        for j in range(steps,len(image)-steps):
            if image[i][j] == '#':
                cnt += 1
    return cnt


with open('i.txt', 'r') as f:
    algo = f.readline()
    image = [list(line.strip()) for line in f.readlines()]
    image = image[1:]
print('p1=', count_lighs_on(image, 2))
print('p2=', count_lighs_on(image, 50))

