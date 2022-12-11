import re


class Monkey:
    def __init__(self, items, operation, test, throw):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw = throw
        self.held = 0


file = open('inputs/input-2022-11.txt')
# file = open('test.txt')


def round(barrel):
    for m in barrel:
        o = m.operation

        for i in m.items:
            m.held += 1
            # monkey inspects items
            if o[2] == 'old':
                num = i
            else:
                num = int(o[2])

            if o[1] == '+':
                i += num
            elif o[1] == '-':
                i -= num
            elif o[1] == '*':
                i *= num
            elif o[1] == '/':
                i /= num

            # monkey gets bored
            i = int(i/3)

            # print(m.throw)
            throw = m.throw
            # decides and throws to a new monkey
            if i % m.test == 0:
                # print(throw[0])
                # print('b',barrel[throw[0]].items)
                barrel[throw[0]].items.append(i)
            else:
                # print(throw[1])
                # print('b',barrel[throw[1]].items)
                barrel[throw[1]].items.append(i)
        m.items = []
    return barrel


munk = []
buff = []
for line in file:
    if line == "\n":
        buff.append(munk)
        munk = []
    else:
        munk.append(line.strip())
buff.append(munk)

barrel = []  # barrel of monkeys haha
for m in buff:
    c1 = m[1].find(':')
    i = re.split('[, ]+', m[1][c1+2:])
    i = [int(j) for j in i]

    c2 = m[2].find(':')
    e = m[2][c2+1:].split()

    c3 = m[3].find('by')
    t = int(m[3][c3+2:])

    c4 = m[4].find('y')
    c5 = m[5].find('y')
    throw = [int(m[4][c4+1:]), int(m[5][c5+1:])]  # [true, false]

    ape = Monkey(i, e[2:], t, throw)
    barrel.append(ape)


for i in range(20):
    barrel = round(barrel)

h = []
for i in barrel:
    h.append(i.held)
h.sort()

print(h[-1]*h[-2])
