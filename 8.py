from os import stat
from typing import Any, List, AnyStr
import statistics
import math

# Part 1 - Naive
file = open("8.txt")
lines = file.readlines()
lines = list(map(str.strip, lines))
file.close()


def parseLine(line: AnyStr):
    return line.strip().replace(" | ", " ").split(" ")


lines = list(map(parseLine, lines))

one = 0
four = 0
seven = 0
eight = 0


def countNums(string):
    global one, four, seven, eight
    num = len(string)
    if num == 2:
        one += 1
    elif num == 4:
        four += 1
    elif num == 3:
        seven += 1
    elif num == 7:
        eight += 1


def printLine(line, map):
    for digit in line:
        if map[0] in digit:
            print(f' {map[0]}{map[0]}{map[0]}{map[0]}')
        else:
            print("")
        if map[1] in digit and map[2] in digit:
            print(f'{map[1]}    {map[2]}\n{map[1]}    {map[2]}')
        elif map[1] in digit:
            print(f'{map[1]}\n{map[1]}')
        elif map[2] in digit:
            print(f'     {map[2]}\n     {map[2]}')
        else:
            print("\n")
        if map[3] in digit:
            print(f' {map[3]}{map[3]}{map[3]}{map[3]}')
        else:
            print("")
        if map[4] in digit and map[5] in digit:
            print(f'{map[4]}    {map[5]}\n{map[4]}    {map[5]}')
        elif map[4] in digit:
            print(f'{map[4]}\n{map[4]}')
        elif map[5] in digit:
            print(f'     {map[5]}\n     {map[5]}')
        else:
            print("\n")
        if map[6] in digit:
            print(f' {map[6]}{map[6]}{map[6]}{map[6]}')
        else:
            print("")
        print("------")


digits = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab cdfeb fcadb cdfeb cdbaf".split(
    " ")

for line in lines:
    for i in range(-4, 0):
        countNums(line[i])

print(one, four, seven, eight, " += ", one + four + seven + eight)


def limitPossibilites(possibleMap: List[List[Any]], i, digit):
    for ind in i:
        possibleMap[ind] = list(set(possibleMap[ind]) & set(digit))
    for ind in range(7):
        if ind not in i:
            possibleMap[ind] = list(set(possibleMap[ind]) - set(digit))


def checkOnePossibleDigit(line, possibleMap):
    for digit in line:
        lit = len(digit)
        splitDigit = list(digit)
        if lit == 2:
            limitPossibilites(possibleMap, [2, 5], splitDigit)
        elif lit == 4:
            limitPossibilites(possibleMap, [1, 2, 3, 5], splitDigit)
        elif lit == 3:
            limitPossibilites(possibleMap, [0, 2, 5], splitDigit)


def areValidNums(line, possibleMap):
    zero = [True, True, True, False, True, True, True]
    one = [False, False, True, False, False, True, False]
    two = [True, False, True, True, True, False, True]
    three = [True, False, True, True, False, True, True]
    four = [False, True, True, True, False, True, False]
    five = [True, True, False, True, False, True, True]
    six = [True, True, False, True, True, True, True]
    seven = [True, False, True, False, False, True, False]
    eight = [True, True, True, True, True, True, True]
    nine = [True, True, True, True, False, True, True]

    nums = [zero, one, two, three, four, five, six, seven, eight, nine]
    for digit in line:
        dig = [False, False, False, False, False, False, False]
        for i in range(7):
            if possibleMap[i] in digit:
                dig[i] = True
        if dig not in nums:
            return False
    return True


def sumOutput(line, digitMap):
    zero = [True, True, True, False, True, True, True]
    one = [False, False, True, False, False, True, False]
    two = [True, False, True, True, True, False, True]
    three = [True, False, True, True, False, True, True]
    four = [False, True, True, True, False, True, False]
    five = [True, True, False, True, False, True, True]
    six = [True, True, False, True, True, True, True]
    seven = [True, False, True, False, False, True, False]
    eight = [True, True, True, True, True, True, True]
    nine = [True, True, True, True, False, True, True]

    nums = [zero, one, two, three, four, five, six, seven, eight, nine]
    sum = 0
    for digit in line[-4:]:
        dig = [False, False, False, False, False, False, False]
        for i in range(7):
            if digitMap[i] in digit:
                dig[i] = True
        sum = sum * 10 + nums.index(dig)
    return sum


def getPermutations(splitMap):
    final = [splitMap.pop(0)]
    return permInternal(final, splitMap)


def permInternal(perms, rem):
    newPerms = []
    for char in rem.pop(0):
        for perm in perms:
            if char not in perm:
                newPerm = perm.copy()
                newPerm.append(char)
                newPerms.append(newPerm)
    if (len(rem) > 0):
        newPerms = permInternal(newPerms, rem)
    return newPerms


def decodeLine(line):
    possibleMap = ["abcdefg", "abcdefg", "abcdefg",
                   "abcdefg", "abcdefg", "abcdefg", "abcdefg"]
    splitMap = list(map(list, possibleMap))
    checkOnePossibleDigit(line, splitMap)
    permutations = getPermutations(splitMap)
    digitMap = []
    for perm in permutations:
        if areValidNums(line, perm):
            digitMap = perm
    return sumOutput(line, digitMap)


finalSum = sum(list(map(decodeLine, lines)))
print(list(map(decodeLine, lines)))
print("FINAL SUM:", finalSum)
