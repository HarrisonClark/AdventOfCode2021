from typing import List
import numpy as np

# Part 1 - Naive
file = open("6.txt")
lines = file.readlines()
lines = list(map(str.strip, lines))
file.close()

fishes = list(map(int, lines[0].split(",")))


def newDay(fishes):
    for i in range(len(fishes)):
        if fishes[i] > 0:
            fishes[i] -= 1
        else:
            fishes[i] = 6
            fishes.append(8)


for i in range(80):
    newDay(fishes)
print(len(fishes))

# Part 2 - Optimized
file = open("6.txt")
lines = file.readlines()
lines = list(map(str.strip, lines))
file.close()

fishes = list(map(int, lines[0].split(",")))

life = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for fish in fishes:
    life[fish] += 1


def newDayLife(life):
    oldFish = life[0]
    newFish = life[0]
    for i in range(1, 9):
        life[i-1] = life[i]

    life[8] = 0
    life[6] += oldFish
    life[8] += newFish


print(life)
for i in range(256):
    newDayLife(life)
print(life)
totalFish = 0
for i in range(9):
    totalFish += life[i]

print(totalFish)
