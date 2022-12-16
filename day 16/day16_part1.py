import os
import re

os.system("aocd > inputs/input-2022-16.txt")


# file = open('inputs/input-2022-16.txt')
file = open('test.txt')


class Valve():
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels


valvs = []
for line in file:
    print(line)
    s = re.split(
        "[Valve  has flow rate=; tunnels lead to valves ,]+", line.strip())
    valvs.append(Valve(s[1], int(s[2]), s[3:]))

for i in valvs:
    print(i.name, i.tunnels)
