import os
import re

# os.system("aocd > inputs/input-2022-15.txt")

file = open("inputs/input-2022-15.txt")


class Sensor():
    def __init__(self, x, y, closeBec):
        self.x = x
        self.y = y
        self.closeBec = closeBec

    def dist(self):
        xDel = abs(self.x-self.closeBec[0])
        yDel = abs(self.y-self.closeBec[1])
        return xDel + yDel


sens = set()
beacons = set()
for line in file:
    nums = re.findall("\-?\d+", line)
    bec = (int(nums[2]), int(nums[3]))
    beacons.add(bec)
    sens.add(Sensor(int(nums[0]), int(nums[1]), bec))


y = 2000000

taken = set()
for s in sens:
    yDif = abs(y-s.y)
    if yDif <= s.dist():
        spots = abs(s.dist()-yDif)
        for i in range(s.x-spots, s.x+spots+1, 1):
            if (i, y) not in beacons:
                taken.add(i)


print(len(taken))
