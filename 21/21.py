#!/usr/bin/env python3
# https://adventofcode.com/2021/day/21
from collections import Counter
import sys
sys.path.append('..')
from timing import timer


def move(player_position, movement):
    for _ in range(movement):
        player_position += 1
        if player_position == 11:
            player_position = 1
    return player_position


def roll_dice(last):
    roll = last + 1
    if roll == 101:
        roll = 1
    return roll


def turn(position, score, dice_last):
    movement = 0
    for _ in range(3):
        dice_last = roll_dice(dice_last)
        position = move(position, dice_last)
    score += position
    return position, score, dice_last


def part1(p1,s1,p2,s2): 
    dice_last = 0
    rolls = 0
    while True:
        p1,s1, dice_last = turn(p1,s1, dice_last)
        rolls += 3
        if s1 > 999:
            break
        p2,s2, dice_last = turn(p2,s2, dice_last)
        rolls += 3
        if s2 > 999:
            break

    print('p1 =', min(s1,s2)*rolls)


def dirac_turn(p1, s1, p2, s2, who):
    global games, w1, w2
    if not who:
        for d1 in [1,2,3]:
            for d2 in [1,2,3]:
                for d3 in [1,2,3]:
                    p = move(p1, d1+d2+d3)
                    s = s1 + p
                    if s >= WIN:
                        w1 += games[(p1,s1,p2,s2,who)]
                    else:
                        games[(p,s,p2,s2, True)] += games[(p1,s1,p2,s2,who)]
    else:
        for d1 in [1,2,3]:
            for d2 in [1,2,3]:
                for d3 in [1,2,3]:
                    p = move(p2, d1+d2+d3)
                    s = s2 + p
                    if s >= WIN:
                        w2 += games[(p1,s1,p2,s2,who)]
                    else:
                        games[(p1,s1,p,s, False)] += games[(p1,s1,p2,s2,who)]
    
    del games[(p1,s1,p2,s2, who)]



@timer
def part2():
    while len(games) != 0:
        #print('universe possibilites atm:', len(games), 'universes', sum(games.values()), 'w1', w1, 'w2', w2)
        keys = list(games)
        p1,s1,p2,s2,who = keys[0]
        dirac_turn(p1,s1,p2,s2,who)
    print('p2 =', max(w1,w2))

# example input
# p1 = 4
# p2 = 8

# my input
p1 = 7
p2 = 10

s1 = 0
s2 = 0

# part 1
part1(p1,s1,p2,s2)

# part 2
WIN = 21 
w1, w2 = 0,0  
games = Counter()
games[(p1,s1,p2,s2, False)] += 1

part2()

