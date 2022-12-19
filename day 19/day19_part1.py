import os
import re

os.system("aocd > inputs/input-2022-19.txt")

# file = open("inputs/input-2022-19.txt")
file = open("day 19/test.txt")


class Blueprint:
    def __init__(self, ID, ore, clay, obsidian, geode):
        self.ID = ID
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def show(self):
        print("blueprint: ", self.ID)
        print("ore cost: ", self.ore)
        print("clay cost: ", self.clay)
        print("obsidian cost: ", self.obsidian)
        print("geode cost: ", self.geode)


buff = []

for line in file:
    buff.append(
        re.split("[Blueprint : Each robot costs. ore clay obsidian geode]+", line.strip()))

plans = {}
for i in buff:
    plans[int(i[1])] = Blueprint(i[1], i[2], i[3], (i[4], i[5]), (i[6], i[7]))

# for i in range(len(plans)):
plans[1].show()
