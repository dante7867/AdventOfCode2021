#!/usr/bin/env python3
# https://adventofcode.com/2021/day/19
import math
import itertools


class Scanner():
    def __init__(self,n,x,y,z):
        self.n = n
        self.x = x
        self.y = y
        self.z = z
        self.default = []
        self.poss = []
        self.established = None
    def __repr__(self):
        repre = f'Scanner {self.n}: ({self.x},{self.y},{self.z})\n'
        default_str = ""
        return repre


    def get_all_possiblities(self):
        self.poss = []
        for i in range(48):
            self.poss.append([])
        for b in self.default:
            i = 0
            for l in itertools.permutations(b):
                for px in [-1,1]:
                    for py in [-1,1]:
                        for pz in [-1,1]:
                            possi = [px*l[0],py*l[1],pz*l[2]]
                            self.poss[i].append(possi)
                            i += 1


def get_pdiff(possibility_points, new_center):
    pdiff = set() 
    
    for poss_point in possibility_points:
        pdiff.add(tuple([poss_point[0]-new_center[0], poss_point[1]-new_center[1], poss_point[2]-new_center[2]]))
    return pdiff   


def pair_matched(scanner1, scanner2):
    for poss1 in scanner1.poss:
        for poss2 in scanner2.poss:
            for point1 in poss1:
                for point2 in poss2:
                    diff1 = get_pdiff(poss1, point1)
                    diff2 = get_pdiff(poss2, point2)
                    d = diff1.intersection(diff2)
                    if len(d) >= 12:
                        scanner2.poss = [poss2]
                        scanner2.established = True
                        return True, point1, point2
    return False, 0, 0


def locate_scanner(base, located):
    success, common_point_base , common_point_located =  pair_matched(base, located)
    if success:
        located.x = base.x + common_point_base[0] - common_point_located[0]
        located.y = base.y + common_point_base[1] - common_point_located[1]
        located.z = base.z + common_point_base[2] - common_point_located[2]
        print(f'Scanner #{located.n} location set...')


def all_established(scanners):
    for s in scanners:
        if not s.established:
            return False
    return True


def locate_all_scanners(scanners):
    while not all_established(scanners):
        for i in range(len(scanners)):
            if scanners[i].established:
                for j in range(len(scanners)):
                    if i != j and not scanners[j].established:
                        locate_scanner(scanners[i], scanners[j])


def calc_manh(scanner1, scanner2):
    return abs(scanner1.x - scanner2.x) + \
            abs(scanner1.y - scanner2.y) + \
            abs(scanner1.z - scanner2.z)


if __name__ == "__main__":
    with open('i.txt', 'r') as f:
        scanners = []
        n = 0 
        for line in f.readlines():
            line = line.strip()
            if line == '':
                scanners.append(scanner)
                n += 1
            elif 'scanner' in line:
                if n == 0:
                    scanner = Scanner(n,0,0,0)
                else:
                    scanner = Scanner(n,'?','?','?')
            else:
                point = line.split(',')
                point = [int(p) for p in point]
                scanner.default.append(point)
    
    scanners[0].poss = [scanners[0].default]
    scanners[0].established = True

    for s in scanners[1:]:
        s.get_all_possiblities()

    locate_all_scanners(scanners)
    
    all_beacons = set()
    for s in scanners:
        beacons = s.poss[0]
        for beacon in beacons:
            rel_0_beacon_x = beacon[0] + s.x
            rel_0_beacon_y = beacon[1] + s.y
            rel_0_beacon_z = beacon[2] + s.z
            all_beacons.add(tuple([rel_0_beacon_x, rel_0_beacon_y, rel_0_beacon_z]))

    print('p1 =', len(all_beacons))

    max_man = 0
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i != j:
                max_man = max(calc_manh(scanners[i], scanners[j]), max_man)
    print('p2 =', max_man)
    
