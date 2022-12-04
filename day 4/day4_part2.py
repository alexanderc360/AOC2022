file = open("inputs/input-2022-4.txt")

list = []
for line in file:
    buff = line.strip().split(',')
    pair = []
    for i in buff:
        pair.append(i.split('-'))
    list.append(pair)

print(list[0])
count = 0
for i in list:
    f = i[0]
    d = i[1]
    fbuff = []
    dbuff = []
    for j in range(int(f[0]), int(f[1])+1, 1):
        fbuff.append(j)
    for j in range(int(d[0]), int(d[1])+1, 1):
        dbuff.append(j)

    if fbuff[0] in dbuff or fbuff[-1] in dbuff:
        count += 1
    elif dbuff[0] in fbuff or dbuff[-1] in fbuff:
        count += 1

print(count)
