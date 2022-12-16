import re
import time

file = open("inputs/input-2022-14.txt")


def show(blocked, rocks):
    min = rocks[0][0]
    max = rocks[0][0]
    for i in blocked:
        for j in blocked[i]:
            if j < min:
                min = j
            elif j > max:
                max = j

    bottom = rocks[0][1]
    for i in rocks:
        if i[1] > bottom:
            bottom = i[1]

    for i in range(len(blocked)+1):
        for j in range(min, max+1, 1):
            if i == len(blocked):
                print('#', end='')
            else:
                if j in blocked[i] and [j, i] in rocks:
                    print('#', end='')
                elif j in blocked[i] and [j, i] not in rocks:
                    print('O', end='')
                else:
                    print('.', end='')

        print()


def genRock(steps):
    rocks = []
    for i in range(len(steps)-1):
        a = steps[i]
        b = steps[i+1]

        xDelta = a[0]-b[0]
        yDelta = a[1]-b[1]
        if abs(xDelta) > 0:
            if xDelta > 0:
                for j in range(a[0], b[0]-1, -1):
                    rocks.append([j, a[1]])
            elif xDelta < 0:
                for j in range(a[0], b[0]+1, 1):
                    rocks.append([j, a[1]])

        if abs(yDelta) > 0:
            if yDelta > 0:
                for j in range(a[1], b[1]-1, -1):
                    rocks.append([a[0], j])
            elif yDelta < 0:
                for j in range(a[1], b[1]+1, 1):
                    rocks.append([a[0], j])
    return rocks


def sandFall(block):
    x = 500  # starting point
    y = 0
    rest = False
    while not rest:
        under = block[y+1]
        if x in under:
            if x - 1 in under:
                if x + 1 in under:
                    rest = True
                    break
                else:
                    x += 1
                    y += 1
            else:
                x -= 1
                y += 1
        else:
            y += 1
        if y + 1 == len(block):
            rest == True
            break

    return [x, y]


rockPlaces = []
for line in file:
    buff = re.split(" -> |,", line.strip())
    buff = [[int(buff[i]), int(buff[i+1])] for i in range(0, len(buff), 2)]
    r = genRock(buff)
    for i in r:
        rockPlaces.append(i)


bottom = 0
for i in rockPlaces:
    if i[1] > bottom:
        bottom = i[1]

blocked = {i: set() for i in range(bottom + 2)}
for i in rockPlaces:
    blocked[i[1]].add(i[0])


start = time.time()
s = 0
while 500 not in blocked[0]:
    s = sandFall(blocked)
    blocked[s[1]].add(s[0])


count = 0
for i in range(len(blocked)):
    for j in blocked[i]:
        if [j, i] not in rockPlaces:
            count += 1

end = time.time()

print('count', count)
print('time: ', end-start, ' seconds')

# show(blocked, rockPlaces)
