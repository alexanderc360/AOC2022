import os

os.system("aocd > inputs/input-2022-3.txt")

file = open("inputs/input-2022-3.txt")
# file = open('test.txt')

for line in file:
    print(line)
