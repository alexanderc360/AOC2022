file = open("inputs/input-2022-10.txt")


sprite = ['.' for i in range(40)]
for i in range(3):
    sprite[i] = '#'

buff = ""
x = 1
cycle = 0
for line in file:
    print(x)
    if line[:4] == 'noop':
        buff += sprite[cycle % 40]
        cycle += 1
    elif line[:4] == 'addx':
        buff += sprite[cycle % 40]
        cycle += 1
        buff += sprite[cycle % 40]
        cycle += 1

        x += int(line[5:])
        sprite = ['.' for i in range(40)]
        for i in range(3):
            sprite[(x-1)+i] = '#'


answer = ''
for i in range(6):
    answer += buff[i*40:i*40+40]
    answer +='\n'
print(answer)