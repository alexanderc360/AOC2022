# file = open("inputs/input-2022-15.txt")
import math
import re

file = open("test.txt")


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
        # print()
    # print(self)
        return a


sens = set()
for line in file:
    print(line)
    nums = re.split("[Sensor at : closest beacon is at =,xy]+", line.strip())
    print(nums)
    bec = (int(nums[3]), int(nums[4]))
    sens.add(Sensor(int(nums[1]), int(nums[2]), bec))

a = set()
for i in sens:
    if i.x == 8 and i.y == 7:
        a = i.area()

for i in range(-2, 16, 1):
    for j in range(0, 18, 1):
        if (j, i) in a:
            print('*', end='')
        else:
            print('.', end='')
    print()
