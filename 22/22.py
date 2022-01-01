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


class Cuboid():
    def __init__(self,x1,x2,y1,y2,z1,z2,toggle = 'on'):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.toggle = True if toggle == 'on' else False
        
        self.valid = False        
        if x2 >= x1 and y2 >= y1 and z2 >= z1:
            self.valid = True


    def points(self):
        return (self.x2-self.x1 + 1) * (self.y2-self.y1 + 1) * (self.z2-self.z1 + 1)


    def __repr__(self):
        return f"Cuboid {self.x1}..{self.x2}, {self.y1}..{self.y2}, {self.z1}..{self.z2}, toggle:{self.toggle}, pts: {self.pts}"

    def __add__(self, cuboid):
        pass

    def __sub__(self, cuboid):
        if not self.intersects_with(cuboid):
            return [self]

        a1 = cuboid.x1
        a2 = cuboid.x2
        b1 = cuboid.y1
        b2 = cuboid.y2
        c1 = cuboid.z1
        c2 = cuboid.z2

        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        z1 = self.z1
        z2 = self.z2

        difference = []
         
        #top
        difference.append( Cuboid(x1, min(a1-1, x2), max(y1, b2+1), y2, z1, min(c1-1,z2) ) )
        difference.append( Cuboid(x1, min(a1-1, x2), max(y1, b2+1), y2, max(c1, z1), min(c2, z2) ) ) 
        difference.append( Cuboid(x1, min(a1-1, x2), max(y1, b2+1), y2, max(z1, c2+1), z2) ) 

        difference.append( Cuboid( max(x1, a1), min(a2, x2), max(y1, b2+1), y2, z1, min(c1-1,z2) ) )
        difference.append( Cuboid( max(x1, a1), min(a2, x2), max(y1, b2+1), y2, max(c1, z1), min(c2, z2) ) )
        difference.append( Cuboid( max(x1, a1), min(a2, x2), max(y1, b2+1), y2, max(c2+1, z1), z2) ) 
        
        difference.append( Cuboid( max(x1, a2 + 1), x2, max(y1, b2+1), y2, z1, min(c1-1,z2) ) ) 
        difference.append( Cuboid( max(x1, a2 + 1), x2, max(y1, b2+1), y2, max(c1, z1), min(c2, z2) ) )
        difference.append( Cuboid( max(x1, a2 + 1), x2, max(y1, b2+1), y2, max(z1, c2+1), z2) )

        # middle
        difference.append( Cuboid(x1, min(a1-1, x2), max(y1, b1), min(y2,b2), z1, min(c1-1,z2) ) )
        difference.append( Cuboid(x1, min(a1-1, x2), max(y1, b1), min(y2,b2), max(c1, z1), min(c2, z2) ) ) 
        difference.append( Cuboid(x1, min(a1-1, x2), max(y1, b1), min(y2,b2), max(z1, c2+1), z2) )

        difference.append( Cuboid( max(x1, a1), min(a2, x2), max(y1, b1), min(y2,b2), z1, min(c1-1,z2) ) )
        ###
        difference.append( Cuboid( max(x1, a1), min(a2, x2), max(y1, b1), min(y2,b2), max(c2+1, z1), z2) ) 
        
        difference.append( Cuboid( max(x1, a2 + 1), x2, max(y1, b1), min(y2,b2), z1, min(c1-1,z2) ) ) 
        difference.append( Cuboid( max(x1, a2 + 1), x2, max(y1, b1), min(y2,b2), max(c1, z1), min(c2, z2) ) )
        difference.append( Cuboid( max(x1, a2 + 1), x2, max(y1, b1), min(y2,b2), max(z1, c2+1), z2) )

        # bottom
        difference.append( Cuboid(x1, min(a1-1, x2), y1, min(y2,b1-1), z1, min(c1-1,z2) ) )
        difference.append( Cuboid(x1, min(a1-1, x2), y1, min(y2,b1-1), max(c1, z1), min(c2, z2) ) ) 
        difference.append( Cuboid(x1, min(a1-1, x2), y1, min(y2,b1-1), max(z1, c2+1), z2) ) 

        difference.append( Cuboid( max(x1, a1), min(a2, x2), y1, min(y2,b1-1), z1, min(c1-1,z2) ) )
        difference.append( Cuboid( max(x1, a1), min(a2, x2), y1, min(y2,b1-1), max(c1, z1), min(c2, z2) ) )
        difference.append( Cuboid( max(x1, a1), min(a2, x2), y1, min(y2,b1-1), max(c2+1, z1), z2) ) 
        
        difference.append( Cuboid( max(x1, a2 + 1), x2, y1, min(y2,b1-1), z1, min(c1-1,z2) ) ) 
        difference.append( Cuboid( max(x1, a2 + 1), x2, y1, min(y2,b1-1), max(c1, z1), min(c2, z2) ) )
        difference.append( Cuboid( max(x1, a2 + 1), x2, y1, min(y2,b1-1), max(z1, c2+1), z2) )
        

        difference = [x for x in difference if x.valid]
        return difference
        

    def intersects_with(self, cuboid):
        return self.x2 >= cuboid.x1 and self.x1 <= cuboid.x2 and \
                self.y2 >= cuboid.y1 and self.y1 <= cuboid.y2 and \
                self.z2 >= cuboid.z1 and self.z1 <= cuboid.z2


def how_many_cubes_are_on(space):
    count = 0
    for cuboid in space:
        count += cuboid.points()
    return count

def p2(cmds):
    space = []
    for cmd in cmds:
        ins, x1, x2, y1, y2, z1, z2 = cmd
        cuboid = Cuboid(x1,x2,y1,y2,z1,z2, ins)

        if len(space)==0:
            space.append(cuboid)
            continue

        if cuboid.toggle: 
            on = [cuboid]
            for s in space:
                new_on = []
                for o in on:
                    new_on += o - s
                on = new_on
            space += on
        else:
            new_space = []
            for s in space:
                new_space += s - cuboid
            space = new_space

    print('p2 =', how_many_cubes_are_on(space))

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
p2(cmds)

