#!/usr/bin/env python3
# https://adventofcode.com/2021/day/14
from collections import Counter


def count_most_and_least_diff(part_str, template, pairs):
    letter_counter = Counter()
    # first and last mer will not change
    letter_counter[template[0]] += 1
    letter_counter[template[-1]] += 1

    for pair, cnt in pairs.items():
        letter_counter[pair[0]] += cnt
        letter_counter[pair[1]] += cnt

    for letter, cnt in letter_counter.items():
        letter_counter[letter] = int(cnt/ 2)

    maxi = int( max(letter_counter.values()) / 2 )
    mnii = int( min(letter_counter.values()) / 2 )

    print(part_str, max(letter_counter.values()) - min(letter_counter.values()) )


with open('i.txt', 'r') as f:
    template = f.readline().strip()
    insertions = {}
    for l in f.readlines():
        if l != '\n':
            combo, insert  = l.strip().split(' -> ')
            insertions[combo] = insert

    pairs = Counter([template[x-1]+template[x] for x in range(1, len(template))])
    
    replacements = {}
    for k,v in insertions.items():
        replacements[k] = [k[0]+v, v+k[1]]

for x in range(40):
    new = Counter()
    for pair, cnt in pairs.items():
        for rep in replacements[pair]:
            new[rep] += cnt 
    pairs = new
    if x == 9: # for 10th step
        count_most_and_least_diff('p1 =', template, pairs)
count_most_and_least_diff('p2 =', template, pairs)
    
