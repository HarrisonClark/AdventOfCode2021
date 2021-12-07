# Part 1
file = open("2.txt")
lines = file.readlines()

x = 0
y = 0

for line in lines:
    dir, amt = line.strip().split(maxsplit=1)
    if dir == "forward":
        x += int(amt)
    elif dir == "down":
        y += int(amt)
    elif dir == "up":
        y -= int(amt)


print(f'Moved x: {x}, y: {y}, x*y: {x*y}')
file.close()

# Part 2
file = open("2.txt")
lines = file.readlines()

aim = 0
x = 0
y = 0

for line in lines:
    dir, amt = line.strip().split(maxsplit=1)
    # print(dir, amt, aim, x, y)
    if dir == "forward":
        x += int(amt)
        y += aim * int(amt)
    elif dir == "down":
        aim += int(amt)
    elif dir == "up":
        aim -= int(amt)

print(f'Moved x: {x}, y: {y}, x*y: {x*y}')
file.close()
