file = open("inputs/input-2022-3.txt")

half = 0
sacks = []
for line in file:
    half = int(len(line.strip())/2)
    fst = line[:half]
    snd = line[half:]
    sacks.append([fst, snd])

buff = []
for i in sacks:
    for j in i[0]:
        if j in i[1]:
            buff.append(j)
            break


sum = 0
for i in buff:
    o = ord(i)
    if o <= 90:
        val = o - 64 + 26
    elif o >= 97:
        val = o - 96
    sum = sum + val


print(sum)
