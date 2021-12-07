# Part 1
file = open("1.txt")
lines = file.readlines()

prev = int(lines.pop(0))
incr = 0

for line in lines:
    this = int(line)
    if (this > prev):
        incr += 1
    prev = this

print(f'Next int increases count:      {incr}')
file.close()

# Part 2
file = open("1.txt")
lines = file.readlines()

window = [int(lines.pop(0)), int(lines.pop(0)), int(lines.pop(0))]
prevSum = sum(window)
incr = 0

for line in lines:
    window.pop(0)
    window.append(int(line))
    thisSum = sum(window)
    if (thisSum > prevSum):
        incr += 1
    prevSum = thisSum

print(f'3int window increases count:   {incr}')
file.close()
