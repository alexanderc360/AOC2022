import os

# os.system("aocd > inputs/input-2022-5.txt")

file = open("inputs/input-2022-5.txt")


cols = []
numLine = 0

for i in file:
    numLine += 1
    if '1' in i:
        cols = i.split()
        break

file = open("inputs/input-2022-5.txt")

count = 0
stacks = [[] for i in range(len(cols))]
steps = []


for line in file:
    count += 1

    for i in range(len(line)-1):
        if line[i] == '[':
            stacks[int(i / 4)].append(line[i+1])

    ins = line.split()
    if count > numLine+1:
        steps.append([ins[1], ins[3], ins[5]])

for s in stacks:
    s = s.reverse()

for i in steps:
    i = [int(j) for j in i]
    for k in range(i[0]):
        stacks[i[2]-1].append(stacks[i[1]-1].pop())


result = ""
for s in stacks:
    result += s.pop()

print(result)
