file = open("inputs/input-2022-1.txt")
# file = open("test.txt")

cal = []
buff = []
for line in file:
    if line != '\n':
        buff.append(int(line.strip()))
    else:
        cal.append(buff)
        buff = []
cal.append(buff)

sums = []
for i in cal:
    sum = 0
    for j in i:
        sum = sum + j
    sums.append(sum)

sums.sort(reverse=True)

# answer
print(sums[0]+sums[1]+sums[2])
