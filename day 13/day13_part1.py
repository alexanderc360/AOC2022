import os

os.system("aocd > inputs/input-2022-13.txt")

# file = open("inputs/input-2022-13.txt")
file = open("test.txt")


def compare(first, second):
    print(type(first), type(second))

    while len(first) > 0 and len(second) > 0:
        f = first.pop()
        s = second.pop()
        print(f, s)

    print()


pairs = []
buff = []
for line in file:
    if line == '\n':
        pairs.append(buff)
        buff = []
    else:
        buff.append(line.strip())
pairs.append(buff)

# for i in pairs:
#     compare(i[0], i[1])


a = [1, 2, 3]
b = [1, 2, 1]

c = compare(a, b)
print(c)
# for i in pairs:
# print(i)
