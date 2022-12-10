file = open("inputs/input-2022-10.txt")

x = 1
cycle = [1]
for line in file:
    if line[:4] == 'noop':
        cycle.append(x)
    elif line[:4] == 'addx':
        cycle.append(x)
        x += int(line[5:])
        cycle.append(x)


print((20*cycle[19]) + (60*cycle[59]) + (100*cycle[99]) +
      (140*cycle[139]) + (180*cycle[179]) + (220*cycle[219]))
