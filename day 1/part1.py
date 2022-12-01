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

max = 0
for i in cal:
    sum = 0
    for j in i:
        sum = sum + j
    if sum > max:
        max = sum

# answer
print(max)