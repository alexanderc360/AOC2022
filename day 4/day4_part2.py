import re

file = open("inputs/input-2022-4.txt")

pairs = []
for line in file:
    buff = re.split(',|-', line.strip())
    pairs.append([buff[0], buff[1], buff[2], buff[3]])

count = 0
for i in pairs:
    fbuff = range(int(i[0]), int(i[1])+1, 1)
    dbuff = range(int(i[2]), int(i[3])+1, 1)

    if fbuff[0] in dbuff or fbuff[-1] in dbuff:
        count += 1
    elif dbuff[0] in fbuff or dbuff[-1] in fbuff:
        count += 1

print(count)
