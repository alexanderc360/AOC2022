import re

# os.system("aocd > inputs/input-2022-14.txt")

file = open("inputs/input-2022-14.txt")
# file = open("test.txt")


def show(rocks, sand):
    min = rocks[0][0]
    max = rocks[0][0]
    bottom = rocks[0][1]

    for i in sand:
        if i[0] < min:
            min = i[0]
        elif i[0] > max:
            max = i[0]

        if i[1] > bottom:
            bottom = i[1]

    for j in range(bottom+1):
        for i in range(min, max+1, 1):
            if [i, j] in rocks:
                print('#', end='')
            elif [i, j] in sand:
                print('O', end='')
            else:
                print('.', end='')
        print('\n')


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


def sandFall(rocks, sand):
    x = 500  # starting point
    y = 0
    rest = False
    bottom = rocks[0][1]
    for i in rocks:
        if i[1] > bottom:
            bottom = i[1]
    while not rest:
        if y > bottom:
            print(bottom)
            return -1
        down = [x, y+1]
        left = [x-1, y+1]
        right = [x+1, y+1]
        blockUnder = down in rocks or down in sand
        blockLeft = left in rocks or left in sand
        blockRight = right in rocks or right in sand

        if blockUnder:
            if blockLeft:
                if blockRight:
                    rest = True
                else:
                    x += 1
                    y += 1
            else:
                x -= 1
                y += 1
        else:
            y += 1

    return [x, y]


rockPlaces = []
for line in file:
    buff = re.split(" -> |,", line.strip())
    buff = [[int(buff[i]), int(buff[i+1])] for i in range(0, len(buff), 2)]
    r = genRock(buff)
    for i in r:
        rockPlaces.append(i)


sandPlaces = []


s = 0
while s != -1:
    s = sandFall(rockPlaces, sandPlaces)
    if type(s) == list:
        sandPlaces.append(s)

show(rockPlaces, sandPlaces)
