#!/usr/bin/env python3
# https://adventofcode.com/2021/day/3
from copy import deepcopy


def p1_bit_shift():
    gamma = 0
    epsilon = 0

    mask = 1
    for x in range(0, width):
        ones = 0
        for num in nums:
            if num & mask:
                ones += 1
        if ones > len(nums) / 2:
            gamma |= mask
        else:
            epsilon |= mask
        mask <<= 1

    # print("{0:b}".format(gamma),",", gamma)
    # print("{0:b}".format(epsilon),",", epsilon)
    return gamma * epsilon


def p1_strings():
    with open('i.txt', 'r') as f:
        strings = [line.strip() for line in f.readlines()]

    gamma, epsilon = "", ""
    width = len(strings[0])
    for x in range(0, width):
        ones = 0
        for l in strings:
            if l[x] == '1':
                ones += 1
        if ones > len(nums) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    # print(f"{gamma} , {(int(gamma, 2))}")
    # print(f"{epsilon} , {(int(epsilon, 2))}")
    return int(epsilon, base=2) * int(gamma, base=2)


def dominant_bit(mask, li):
    ones = 0
    for l in li:
        if l & mask:
            ones += 1
    if ones >= len(li) / 2:
        return mask
    return 0


def p2(carbon, oxygen, width):
    mask = 1
    for _ in range(width - 1):
        mask <<= 1

    while len(oxygen) > 1:
        dominant = dominant_bit(mask, oxygen)
        oxygen = [x for x in oxygen if (x & mask) == dominant]
        mask >>= 1

    mask = 1
    for _ in range(width - 1):
        mask <<= 1
    while len(carbon) > 1:
        dominant = dominant_bit(mask, carbon)
        carbon = [x for x in carbon if not (x & mask) == dominant]
        mask >>= 1

    return oxygen[0] * carbon[0]


with open('i.txt', 'r') as file:
    nums = [int(line, base=2) for line in file.readlines()]
    file.seek(0)
    width = len(file.readline().strip())

    print(f"{p1_bit_shift() = }")
    print(f"{p1_strings()   = }")
    
    oxygen = nums
    carbon = deepcopy(oxygen)
    print(f"p2 = {p2(carbon, oxygen, width)}")


