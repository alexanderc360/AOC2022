import os

os.system("aocd > inputs/input-2022-6.txt")

file = open("inputs/input-2022-6.txt")

line = file.readline()


def unique(list):
    for i in range(len(list)):
        if list[i] in list[i+1:]:
            return False
    return True


for i in range(len(line)-3):
    buff = line[i:i+4]
    if unique(buff):
        print(i+4)
        break
