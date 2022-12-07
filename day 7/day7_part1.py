import os

os.system("aocd > inputs/input-2022-7.txt")

# file = open("inputs/input-2022-7.txt")
file = open('test.txt')

# for line in file:
#     print(line)


class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.content = []


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name


cmd = []

for line in file:
    cmd.append(line.strip())

i = 0
cwd = Dir(None, None)
# print(type(cwd) == Dir)

while i < len(cmd):
    if cmd[i] == '':
        break
    line = cmd[i]
    if line[0] == '$':
        if line[2:4] == 'ls':
            for j in cmd[i+1:]:
                if j[0] == '$':
                    break
                else:
                    s = j.find(' ')
                    if j[:s] == 'dir':
                        cwd.content.append(Dir(cwd, j[s+1:]))
                    else:
                        cwd.content.append(File(int(j[:s]), j[s+1:]))
        elif line[2:4] == 'cd':
            if line[5:] == '/':
                cwd = Dir(None, '/')
            elif line[5:] == '..':
                cwd = cwd.parent
            else:
                for k in cwd.content:
                    if type(k) == Dir:
                        if k.name == line[5:]:
                            cwd = k

    # print(i)
    i += 1


def sizeFinder(dir):
    print('dir', dir.name)
    count = 0
    for i in dir.content:
        # print(type(i))
        print('size:', size)
        if type(i) == File:
            print('file: ', i.name, i.size)
            count += i.size
        elif type(i) == Dir:
            # print('dir')
            size = sizeFinder(i, count)
    return size


# while cwd.name != '/':
cwd = cwd.parent


# cwd = cwd.content[0]

# print('DIR:', cwd.name)

# # for i in cwd.content:
#     print(i.name)

s = sizeFinder(cwd, 0)
print(s)
# for i in s:
    # print(i)
