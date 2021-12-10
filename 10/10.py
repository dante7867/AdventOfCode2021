#!/usr/bin/env python3
# https://adventofcode.com/2021/day/10
opens = ['(','[','{','<']
closures = [')',']','}','>']


def get_completion_score(history):
    completion_pts = {'(':1, '[':2, '{':3, '<':4}
    score = 0
    for h in history[::-1]:
            score *= 5
            score += completion_pts[h]
    return score


def p1and2(lines):
    # for p1
    error_score = 0
    error_pts = {')':3,']':57,'}':1197,'>':25137}
    # for p2
    completion_scores = []

    for l in lines:
        history = []
        errorous = False
        for b in l:
            if b in opens:
                history.append(b)
            else:
                if opens.index(history[-1]) == closures.index(b):
                    history.pop()
                else:
                    errorous = True
                    error_score += error_pts[b]
                    break
        if not errorous:
            completion_scores.append(get_completion_score(history))
    
    print('p1 =', error_score)
    print('p2 =', sorted(completion_scores)[int(len(completion_scores)/2)])


with open('i.txt','r') as f:
    lines = [l.strip() for l in f.readlines()]
    p1and2(lines)
