#!/usr/bin/env python3
# https://adventofcode.com/2021/day/17
import sys
sys.path.append("..")
from timing import timer


x1 = 175
x2 = 227
y1 = -134
y2 = -79


def step(x,y, vx,vy):
    x += vx
    y += vy

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    
    return x, y,vx,vy


def estabish_min_horizontal_speed():
    global x1,x2
    speed = 0
    while True:
        speed += 1
        if sum(range(speed + 1)) > x1:
            return speed


@timer
def p1and2():
    max_height_for_all_hitting_angles = 0
    number_of_hitting_angles = 0
    max_vy_that_hits = 0
    for start_vx in range(estabish_min_horizontal_speed(),x2+1):
        for start_vy in range(y1,abs(y1)+1):
            x,y = 0,0
            vx = start_vx
            vy = start_vy
            
            hit = False
            max_height = 0
            while x <= x2 and y >= y1 and not hit:
                x,y,vx,vy = step(x,y,vx,vy)
                hit = x1<=x<=x2 and y1<=y<=y2
                if y > max_height:
                    max_height = y
                if hit:
                    max_height_for_all_hitting_angles = max(max_height_for_all_hitting_angles, max_height) 
                    number_of_hitting_angles += 1

    print(f'p1 = {max_height_for_all_hitting_angles}')
    print(f'p2 = {number_of_hitting_angles}')


if __name__ == "__main__":
    p1and2()
