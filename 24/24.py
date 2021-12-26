#!/usr/bin/env python3
# https://adventofcode.com/2021/day/24


def block(w, z, A, B, C):
    # idx [ 0,  1,  2,  3,  4,   5,  6,   7,  8,  9, 10, 11,  12, 13]
    #   A [ 1,  1,  1,  1,  1,  26,  1,  26, 26,  1, 26, 26,  26, 26]
    #   B [15, 10, 12, 10, 14, -11, 10, -16, -9, 11, -8, -8, -10, -9]
    #   C [13, 16,  2,  8, 11,   6, 12,   2,  2, 15,  1, 10,  14, 10]
    # Digits checking for descendape are those were A == 26. Those are: 5, 7, 8, 10, 11, 12, 13
    # Those indexes will decide if 'z' register will ddescendend

    ddescendend = False

    x=z%26   
    z=z//A  # A can be either '1' or '26'
    x += B     

    x=int(x!=w) 
    if x==0:   # only if x is '0' the numbers will ddescendend, otherwise we want to descendape currently considered number 
        ddescendend = True

    y=1+25*x   
    z*=y
    
    y=w+C 
    y*=x
    z+=y

    return z, ddescendend


def solve(A, B, C, R):
    for one in R:
        z = 0
        z1, _ = block(one, z, A[0], B[0], C[0])
        for two in R:
            z2, _ = block(two, z1, A[1], B[1], C[1])
            for three in R:
                z3, _ = block(three, z2, A[2], B[2], C[2])
                for four in R:
                    z4, _ = block(four, z3, A[3], B[3], C[3])
                    for five in R:
                        z5, _ = block(five, z4, A[4], B[4], C[4])
                        for six in R:
                            z6, descend6 = block(six, z5, A[5], B[5], C[5])
                            if descend6:  # decisive digit
                                for seven in R:
                                    z7, _ = block(seven, z6, A[6], B[6], C[6])
                                    for eight in R:
                                        z8, descend8 = block(eight, z7, A[7], B[7], C[7])
                                        if descend8:  # decisive digit
                                            for nine in R:
                                                z9, descend9 = block(nine, z8, A[8], B[8], C[8])
                                                if descend9: # decisive digit
                                                    for ten in R:
                                                        z10, _ = block(ten, z9, A[9], B[9], C[9])
                                                        for eleven in R:
                                                            z11, descend11 = block(eleven, z10, A[10], B[10], C[10])
                                                            if descend11:  # decisive digit
                                                                for twelve in R:
                                                                    z12, descend12 = block(twelve, z11, A[11], B[11], C[11])
                                                                    if descend12:  # decisive digit
                                                                        for thirteen in R:
                                                                            z13, descend13 = block(thirteen, z12, A[12], B[12], C[12])
                                                                            if descend13:  # decisive digit
                                                                                for fourteen in R:
                                                                                    z14, descend14 = block(fourteen, z13, A[13], B[13], C[13])
                                                                                    if z14==0:  # last decisive digit
                                                                                        return str(one)+str(two)+str(three)+str(four)+str(five)+str(six)+str(seven)+\
                                                                                                str(eight)+str(nine)+str(ten)+str(eleven)+str(twelve)+str(thirteen)+str(fourteen)


with open('i.txt', 'r') as f:
    A,B,C = [], [], []
    lines = [line.strip().split(' ') for line in f.readlines()]
    for i, line in enumerate(lines):
        if i%18 == 4:   # 1st number not common for all blocks is at line 4 for each block
            A.append(int(line[2]))
        if i%18 == 5:   # 2nd number not common for all blocks is at line 5 for each block
            B.append(int(line[2]))
        if i%18 == 15:  # 3rd number not common for all blocks is at line 15 for each block
            C.append(int(line[2]))

print('p1=', solve(A, B, C, range(9,0,-1)))
print('p2=', solve(A, B, C, range(1,10)))

