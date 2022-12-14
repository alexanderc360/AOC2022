import os
import re

os.system("aocd > inputs/input-2022-14.txt")

# file = open("inputs/input-2022-14.txt")
file = open("test.txt")


# start at [500,0] move down
# if point is a rock, sand is at rest
# else point is sand
# if the point to the left is clear, repeat at [x-1,i]
# elsi if the point to the right is clear, repeat at [x-1,i]


def sandDropper(rocks, sand, x, y):
    print(x, y)
    # sand = []
    rockUnder = [x, y+1] in rocks
    sandUnder = [x, y+1] in sand

    if rockUnder:
        sand.append([x, y])
        print('at rest')
        return sand
    elif sandUnder:
        if [x - 1, y] not in sand and [x - 1, y] not in rocks:
            sandDropper(rocks, sand, x-1, y)
        elif [x + 1, y] not in sand and [x + 1, y] not in rocks:
            sandDropper(rocks, sand, x+1, y)
    else:
        sandDropper(rocks, sand, x, y+1)


for line in file:
    # print(line)
    buff = re.split(" -> |,", line.strip())
    places = [[int(buff[i]), int(buff[i+1])] for i in range(0, len(buff), 2)]


rocks = []
for i in range(len(places)-1):
    # print(places[i], ' - > ', places[i+1])
    a = places[i]
    b = places[i+1]
    # rocks.append(a)

    xDelta = a[0]-b[0]
    yDelta = a[1]-b[1]
    # print(yDelta)
    if abs(xDelta) > 0:
        # print('verticle')
        if xDelta > 0:
            for j in range(a[0], b[0]-1, -1):
                rocks.append([j, a[1]])
        elif xDelta < 0:
            for j in range(a[0], b[0]+1, 1):
                rocks.append([j, a[1]])

    if abs(yDelta) > 0:
        # print('horizontal')
        if yDelta > 0:
            for j in range(a[1], b[1]-1, -1):
                rocks.append([a[0], j])
        elif yDelta < 0:
            # print('sup', a[1])
            for j in range(a[1], b[1]+1, 1):
                # print(j)
                rocks.append([a[0], j])

# print()
# for i in rocks:
#     print(i)
# sand = [[500, 8]]
sand = []

sand = sandDropper(rocks, rocks, 500, 0)

# for i in sand:
# print(i)
