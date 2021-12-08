from typing import List
import numpy as np

# Part 1
file = open("5.txt")
lines = file.readlines()
lines = list(map(str.strip, lines))
file.close()


def parseVents(line):
    start, end = line.strip().split(" -> ")
    start = start.split(",")
    end = end.split(",")
    start.extend(end)
    start = list(map(lambda x: int(x), start))
    return start


vents = list(map(parseVents, lines))
maxVent = max(list(map(lambda l: max(l), vents))) + 1
grid = np.zeros((maxVent, maxVent), dtype=int).tolist()


def print2d(grid):
    print("-------------------")
    for line in grid:
        print(line)


def markVents(vent, map):
    x1, y1, x2, y2 = vent
    if (x1 > x2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    if (y1 > y2):
        x1, y1, x2, y2 = x2, y2, x1, y1

    if (x1 == x2):
        for i in range(y1, y2 + 1):
            map[i][x1] += 1

    elif (y1 == y2):
        for i in range(x1, x2 + 1):
            map[y1][i] += 1

    else:
        if x1 < x2:
            for i in range(x2 - x1 + 1):
                map[y1 + i][x1 + i] += 1
        else:
            for i in range(x1 - x2 + 1):
                map[y1 + i][x1 - i] += 1


for vent in vents:
    markVents(vent, grid)

total = 0
for line in grid:
    for pos in line:
        if pos > 1:
            total += 1

print(f'There are {total} overlapping vents')
