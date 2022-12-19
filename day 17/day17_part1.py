# file = open("inputs/input-2022-17.txt")
file = open("test.txt")


def tetris(tower, jets):
    height = len(tower) + 3
    rest = False

    while not rest:
        print(height)
        if height == 0:
            rest = True
        height -= 1

    print(tower)


steps = []
for line in file:
    for i in line:
        steps.append(i)


# for s in steps:
#     if s == '>':
#         print('right')
#     elif s == '<':
#         print('left')


tower = {}

tetris(tower, steps)
