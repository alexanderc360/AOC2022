import os

os.system("aocd > inputs/input-2022-2.txt")

file = open("inputs/input-2022-2.txt")
# file = open('test.txt')

guide = []
for line in file:
    game = line.split()
    guide.append(game)

score = 0
for i in guide:
    if i[0] == 'A':
        if i[1] == 'X':
            score = score + 1 + 3
        elif i[1] == 'Y':
            score = score + 2 + 6
        elif i[1] == 'Z':
            score = score + 3 + 0
    elif i[0] == 'B':
        if i[1] == 'X':
            score = score + 1 + 0
        elif i[1] == 'Y':
            score = score + 2 + 3
        elif i[1] == 'Z':
            score = score + 3 + 6 
    elif i[0] == 'C':
        if i[1] == 'X':
            score = score + 1 + 6
        elif i[1] == 'Y':
            score = score + 2 + 0
        elif i[1] == 'Z':
            score = score + 3 + 3

print(score)
