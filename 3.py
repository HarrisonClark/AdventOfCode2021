# Part 1
file = open("3.txt")
lines = file.readlines()
lines = list(map(str.strip, lines))


def gamma_epsilon(lines):
    sums = []

    for line in lines:
        for x in range(len(line)):
            try:
                sums[x] += int(line[x])
            except:
                sums.append(int(line[x]))

    gamma = ""
    epsilon = ""
    for i in range(len(sums)):
        gamma += str(int(sums[i]/len(lines) + 0.5))
        if sums[i] == len(lines):  # all 1's, least common is 1
            epsilon += "1"
        elif sums[i] == 0:  # all 0's, least common is 0
            epsilon += "0"
        else:
            epsilon += str(1 - int(sums[i]/len(lines) + 0.5))

    return (gamma, epsilon)


gamma, epsilon = gamma_epsilon(lines)
g = int("".join(gamma), 2)
e = int("".join(epsilon), 2)


print(f'Gamma={gamma}, epsilon={epsilon}')
print(f'Gamma={g}, epsilon={e}, g*e={g*e}')

# Part 2

o2 = lines
x = 0

while(len(o2) > 1):
    gamma, _ = gamma_epsilon(o2)
    # if(len(o2) < 10):
    #     print(list(map(lambda string: string[0: x+1], o2)))
    #     print(gamma[x], gamma[0: x+1], x)
    no2 = []
    for line in o2:
        if line[x] == gamma[x]:
            no2.append(line)
    o2 = no2
    x += 1

co2 = lines
x = 0

history = ""
while(len(co2) > 1):
    _, epsilon = gamma_epsilon(co2)
    # if(len(co2) < 10):
    #     print(list(map(lambda string: string[0: x+1], co2)))
    #     print(epsilon[x], epsilon[0: x+1], x)
    nco2 = []
    for line in co2:
        if line[x] == epsilon[x]:
            nco2.append(line)
    co2 = nco2
    history += epsilon[x]
    x += 1

print("history:", history)
o = int("".join(o2), 2)
c = int("".join(co2), 2)

print(f'o2= {o2}, co2= {co2}')
print(f'o2= {o}, co2= {c}, o*c= {o*c}')

file.close()

# Part 2
# 4188156
