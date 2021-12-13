from os import stat
from typing import List
import statistics
import math

# Part 1 - Naive
file = open("7.txt")
lines = file.readlines()
lines = list(map(str.strip, lines))
file.close()

crabs = list(map(int, lines[0].split(",")))
median = statistics.median(crabs)

fuel = sum(map(lambda x: abs(x - median), crabs))

print("Part 1: median to find center")
print(median, fuel)

print("Part 2: avg to find center")
average = int(statistics.fmean(crabs))
fuel = sum(map(lambda x: abs(x-average) * (abs(x-average) + 1) / 2, crabs))
print(average, fuel)

print("Part 2: iteratively")
min = min(crabs)
max = max(crabs)
minFuel = -1
pos = 0
for i in range(min, max+1):
    fuel = sum(map(lambda x: abs(x-i) * (abs(x-i) + 1) / 2, crabs))
    if fuel < minFuel or minFuel == -1:
        minFuel = fuel
        pos = i

print(pos, minFuel)
