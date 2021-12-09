#!/usr/bin/env python3
# https://adventofcode.com/2021/day/8


with open('i.txt','r') as f:
    INOUT = [line.strip().split('|') for line in f.readlines()]
    IN = [io[0].strip().split(' ') for io in INOUT]
    OUT = [io[1].strip().split(' ') for io in INOUT]

    # Sequence of segments does not matter so sort both IN and OUT
    for idx, i in enumerate(IN):
        IN[idx] = ["".join(sorted(x)) for x in i]
    for idx, i in enumerate(OUT):
        OUT[idx] = ["".join(sorted(x)) for x in i]


def p1():
    su = 0
    for o in OUT:
        for digits in o:
            if len(digits) in [2,3,4,7]:
                su += 1
    return su


def decode(line):
    digit2code = {}

    # find (1,4,7,8) by unique number of segments
    for enc in line:
        if len(enc) == 2:
            digit2code[1] = enc
        if len(enc) == 3:
            digit2code[7] = enc
        if len(enc) == 4:
            digit2code[4] = enc
        if len(enc) == 7:
            digit2code[8] = enc

    for enc in line:
        # from (0,6,9) only 6 does not contain 1
        if len(enc) == 6 and not all(s in enc for s in digit2code[1]): 
            digit2code[6] = enc
        # we can find 9 by looking for 4 in it
        elif len(enc) == 6 and all(s in enc for s in digit2code[4]):
            digit2code[9] = enc
        # now we can find 3
        elif len(enc)==5 and all(s in enc for s in digit2code[1]):
            digit2code[3] = enc

    # sweep what we found
    line = [x for x in line if x not in digit2code.values()]
    # (2,5,0) remain to be found
    for enc in line:
        # 9 contains 5
        if len(enc)==5 and all(s in digit2code[9] for s in enc):
            digit2code[5] = enc
        # the only six segment digit left is 0
        elif len(enc) == 6:
            digit2code[0] = enc          
        # the only other option left is 2
        else:
            digit2code[2] = enc

    return {v: k for k, v in digit2code.items()}


def p2():
    su = 0
    for i, o in zip(IN, OUT):
        code2digit = decode(i)
        mul = 1
        for code in o[::-1]:
            su += code2digit[code] * mul
            mul *= 10
    return su

print(f"{p1() = }")
print(f"{p2() = }")

