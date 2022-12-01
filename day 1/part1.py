import os

os.system("aocd > inputs/input-2022-1.txt")

file = open("inputs/input-2022-1.txt")

for line in file:
    print(line)
