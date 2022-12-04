file = open("inputs/input-2022-3.txt")

# seperates lines into groups
count = 0
buff = []
groups = []
for line in file:
    count += 1
    buff.append(line.strip())
    if count == 3:
        count = 0
        groups.append(buff)
        buff = []

# finding group tag
tags = []
for i in groups:
    for j in i[0]:
        if j in i[1] and j in i[2]:
            tags.append(j)
            break
    
# adding priority sum
sum = 0
for i in tags:
    o = ord(i)
    if o <= 90:
        val = o - 64 + 26
    elif o >= 97:
        val = o - 96
    sum = sum + val

print(sum)
