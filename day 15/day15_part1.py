import math
import os
import re

# os.system("aocd > inputs/input-2022-15.txt")

# file = open("inputs/input-2022-15.txt")
file = open("day 15/test.txt")


class Sensor():
    def __init__(self, x, y, closeBec):
        self.x = x
        self.y = y
        self.closeBec = closeBec

    def dist(self):
        xDel = abs(self.x-self.closeBec[0])
        yDel = abs(self.y-self.closeBec[1])
        return xDel + yDel

    def area(self):
        a = set()
        for i in range(self.dist()+1, 0, -1):
            for j in range(i):
                a.add((self.x+j, self.y-i))
                print('*', end='')
            print()
        return a


sens = set()
for line in file:
    # print(line)
    # nums = re.split("[Sensor at :closestbeaconis=,xy]+", line.strip())
    nums = re.findall("\-?\d+", line)
    # print(nums)
    bec = (int(nums[2]), int(nums[3]))
    sens.add(Sensor(int(nums[0]), int(nums[1]), bec))

a = set()
maxX = 0
for i in sens:
    if i.x > maxX:
        maxX = i.x
    # print(i.x, i.y)
# print(maxX)

y = 10

# xDel = abs(self.x-self.closeBec[0])
# yDel = abs(self.y-self.closeBec[1])


count = 0
for i in range(maxX):
    for j in sens:
        xDif = abs(i-j.x)
        yDif = abs(y-j.y)

        if (xDif+yDif) <= j.dist():
            count += 1


# need to account for spots that contain a beacon, then part 1 is done
print(count)
