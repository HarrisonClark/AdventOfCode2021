from typing import List
import numpy as np

# Part 1
file = open("4.txt")
lines = file.readlines()
lines = list(map(str.strip, lines))

randomNums = lines.pop(0).split(",")
randomNums = list(map(int, randomNums))
lines.pop(0)

boards = []
board = []
for line in lines:
    if line == "":
        boards.append(board)
        board = []
    else:
        board.append(list(map(int, line.split())))
boards.append(board)


def isWinner(board, nums: List[int]):
    # Check rows
    for row in board:
        winningRow = True
        for num in row:
            if num not in nums:
                winningRow = False
        if winningRow:
            return True

    for column in np.transpose(board):
        winningColumn = True
        for num in column:
            if num not in nums:
                winningColumn = False
        if winningColumn:
            return True

    return False


def findFirstWinner(boards, randomNums):
    step = 1
    while (step < len(randomNums)):
        for board in boards:
            if isWinner(board, randomNums[:step]):
                return board, step
        step += 1


def findLastWinner(boards, randomNums):
    step = 1
    while (step < len(randomNums)):
        for board in boards:
            if isWinner(board, randomNums[:step]):
                if (len(boards) == 1):
                    return boards[0], step
                boards.remove(board)
        step += 1


def findScore(board, calledNums):
    score = 0
    for row in board:
        for num in row:
            if num not in calledNums:
                print(num, end=" ")
                score += int(num)
            else:
                print("**", end=" ")
        print("")
    return score


winner, steps = findFirstWinner(boards, randomNums)
score = findScore(winner, randomNums[:steps])
print(score, randomNums[steps-1])
print(score * randomNums[steps-1])

winner, steps = findLastWinner(boards, randomNums)
score = findScore(winner, randomNums[:steps])
print(score, randomNums[steps-1])
print(score * randomNums[steps-1])
