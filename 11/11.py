# https://adventofcode.com/2021/day/11


def update_adjacent(y,x):
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if x + dx > -1 and x + dx < len(octo[0]) and y + dy > -1 and y + dy < len(octo):
                octo[y+dy][x+dx] += 1
                if octo[y+dy][x+dx] > 9 and flashed[y+dy][x+dx] == 0:
                    flashed[y+dy][x+dx] = 1
                    update_adjacent(y+dy,x+dx)


with open('i.txt','r') as f:
    octo = [list(line.strip()) for line in f.readlines()]
    for i, c in enumerate(octo):
        octo[i] = [int(x) for x in c]

flashes = 0
step = 0
common = False
while not common or step < 100:
    step += 1
    common = True
    flashed = [[0]*len(octo[0]) for row in octo]

    # 1 current step energy increase
    for i, c in enumerate(octo):
        octo[i] = [x+1 for x in c]
    # 2 flashes and their energy distribution
    for y in range(len(octo)):
        for x in range(len(octo[0])):
            if octo[y][x] > 9 and flashed[y][x] == 0:
                flashed[y][x] = 1
                update_adjacent(y,x)
    # 3 counting flashes, reseting energy for flashing octopuses
    for y, c in enumerate(octo):
        for x, r in enumerate(octo[y]):
            if octo[y][x] > 9:
                flashes +=  1
                octo[y][x] = 0
    # p2 - check for simultaneous flash
    for y, c in enumerate(octo):
        for x, r in enumerate(octo[y]):
            if octo[y][x] != 0:
                common = False
                break
        if not common:
            break

    if step == 100:
        print('p1 =', flashes)
    if common:
        print('p2 =', step)


