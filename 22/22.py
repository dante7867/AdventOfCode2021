#!/usr/bin/env python3
# https://adventofcode.com/2021/day/22

import re


def should_skip(x1, x2, y1, y2, z1, z2):
    if x1 < -50 or x2 > 50 or \
            y1 < -50 or y2 > 50 or \
            z1 < -50 or z2 > 50:
                return True
    return False


def p1(cmds):
    on = set()
    for cmd in cmds:
        ins, x1, x2, y1, y2, z1, z2 = cmd
        
        if should_skip(x1, x2, y1, y2, z1, z2):
            continue

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    if ins == 'on':
                        on.add(tuple([x,y,z]))
                    if ins == 'off':
                        on.discard(tuple([x,y,z]))

    print('p1 =', len(on))



#p1(cmds)

class Cube():
    def __init__(self,x1,x2,y1,y2,z1,z2,toggle = 'on'):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.valid = False
        self.toggle = toggle
        self.pts = (self.x2-self.x1 + 1) * (self.y2-self.y1 + 1) * (self.z2-self.z1 + 1)

        if x2 >= x1 and y2 >= y1 and z2 >= z1:
            self.valid = True


    def points(self):
        return (self.x2-self.x1 + 1) * (self.y2-self.y1 + 1) * (self.z2-self.z1 + 1)


    def __repr__(self):
        return f"Cube {self.x1}..{self.x2}, {self.y1}..{self.y2}, {self.z1}..{self.z2}, toggle:{self.toggle}, valid: {self.valid}, pts: {self.pts}"

    def __add__(self, cube):
        pass

    def __sub__(self, cube):
        print('substracting\n', self, '\nminus\n', cube, '\n---------')      
        a1 = cube.x1
        a2 = cube.x2
        b1 = cube.y1
        b2 = cube.y2
        c1 = cube.z1
        c2 = cube.z2

        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        z1 = self.z1
        z2 = self.z2

        DIFFERENCE = []
        
         
        # top 
        CUBES.append( Cube(x1, min(a1-1, x2-1), max(b2+1, y1), y2, z1, min(c1-1,z2-1) ) )
        # top 2 
        CUBES.append( Cube(x1, min(a1-1, x2-1), max(b2+1, y1), y2, b1, min(b2, z2-1) ) )
        # top 3
        CUBES.append( Cube(x1, min(a-1, x2-1), max(b2+1, y1), y2, max(b2+1, z1), z2 ) )


        return DIFFERENCE
        
    def contains(self, cube):
        one = self.x1 <= cube.x1 <= self.x2 
        two = self.x1 <= cube.x2 <= self.x2
        three = self.y1 <= cube.y1 <= self.y2
        four = self.y1 <= cube.y2 <= self.y2
        five = self.z1 <= cube.z1 <= self.z2
        six = self.z1 <= cube.z2 <= self.z2
        return one and two and three and four and five and six


def test1():
    c1 = Cube(4,6,4,6,4,6)
    c2 = Cube(0,3,0,3,0,3)
    leftovers = c1-c2
    su = 0
    print('*'*30)
    for l in leftovers:
        print(l)
        su += l.points()
    print('su1', su)
    print('*'*30)
def test2():
    su = 0
    c3 = Cube(0,5,0,5,0,5)
    print(c3)
    c4 = Cube(0,5,2,3,2,3) 
    print(c4)
    leftovers = c3-c4
    print('*'*30)
    for l in leftovers:
        print(l)
        su += l.pts
    print('su1', su)
    print('*'*30)
def test3():
    su = 0
    c5 = Cube(0,5,0,5,0,5)
    print('c5 points', c5.points())
    leftovers = c5-c5
    print('*'*30)
    for l in leftovers:
        print(l)
        su += l.points()
    print('su1', su)
    print('*'*30)
def test4():
    su = 0
    c6 = Cube(0,5,0,5,0,5)
    c7 = Cube(-6,-1,0,5,0,5)
    print(c6)
    print(c7)
    print('*'*30)
    leftovers = c7-c6
    print('*'*30)
    for l in leftovers:
        print(l)
        su += l.points()
    print('su1', su)
    print('*'*30)
def test5():
    su = 0
    c6 = Cube(-20,26,-36,17,-47,7)
    c7 = Cube(-20,33,-21,23,-26,28)
    print(c6)
    print(c7)
    print('*'*30)
    leftovers = c7-c6
    for l1 in leftovers:
        for l2 in leftovers:
            if l1 != l2:
                pass
    print('*'*30)
    for l in leftovers:
        print(l)
        su += l.points()
    print('su1', su)
    print('*'*30)


#test5()


with open('i.txt', 'r') as f:
    cmds = []
    r = r'^(on|off)\sx=(-?\d*\.{0,1}\d+)..(-?\d*\.{0,1}\d+),y=(-?\d*\.{0,1}\d+)..(-?\d*\.{0,1}\d+),z=(-?\d*\.{0,1}\d+)..(-?\d*\.{0,1}\d+)$'
    for line in f.readlines():
        m = re.search(r, line)
        cmd = [m.group(1)]
        for i in range(2,8):
            cmd.append(int(m.group(i)))
        cmds.append(cmd)

p1(cmds)

"""
def eval_space(space):
    su = 0
    for cube in space:
        su += cube.points()
    print('enlighted points:', su)
    return su

cubes = []
for cmd in cmds:
    ins, x1, x2, y1, y2, z1, z2 = cmd
    if should_skip(x1, x2, y1, y2, z1, z2):
        continue
    cube = Cube(x1,x2,y1,y2,z1,z2, ins)
    if cube.valid:
        cubes.append(cube)

print('*'*30)

space = []
diff = cubes[0] - cubes[1]
for d in diff:
    print('diff', d)
eval_space(space)
"""


# 71328
