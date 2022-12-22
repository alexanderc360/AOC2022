import re
import time

file = open('inputs/input-2022-21.txt')


def monkeyMath(curMonkey, monks):
    val = monks[curMonkey]
    if re.search("[0-9]+", val):
        return int(val)
    else:
        if '+' in val:
            buff = val.split('+')
            return monkeyMath(buff[0], monks) + monkeyMath(buff[1], monks)
        elif '-' in val:
            buff = val.split('-')
            return monkeyMath(buff[0], monks) - monkeyMath(buff[1], monks)
        elif '*' in val:
            buff = val.split('*')
            return monkeyMath(buff[0], monks) * monkeyMath(buff[1], monks)
        elif '/' in val:
            buff = val.split('/')
            return monkeyMath(buff[0], monks) / monkeyMath(buff[1], monks)


start = time.time()
monkeys = {}
for line in file:
    line = line.strip().replace(' ', '').split(':')

    monkeys[line[0]] = line[1]


answer = monkeyMath('root', monkeys)
print('answer', answer)
end = time.time()

print(end-start)
