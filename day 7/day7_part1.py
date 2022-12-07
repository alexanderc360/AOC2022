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
    # print(cwd.name)
    if cmd[i] == '':
        break
    line = cmd[i]
    if line[0] == '$':
        # print(line)
        if line[2:4] == 'ls':
            # print('ls')
            for j in cmd[i+1:]:
                if j[0] == '$':
                    break
                else:
                    s = j.find(' ')
                    if j[:s] == 'dir':
                        cwd.content.append(Dir(cwd, j[s+1:]))
                        # print(j)
                    else:
                        cwd.content.append(File(int(j[:s]), j[s+1:]))
                        # print(j)
        elif line[2:4] == 'cd':
            # print('cd ', line[5:])
            if line[5:] == '/':
                cwd = Dir(None, '/')
                # print(cwd.name)
            elif line[5:] == '..':
                # print('f')
                cwd = cwd.parent
                # print(cwd.name)
            else:
                # print()
                for k in cwd.content:
                    if type(k) == Dir:
                        if k.name == line[5:]:
                            cwd = k

    # print(i)
    i += 1


def sizeFinder(dir, size):
    # print(dir.name)
    for i in dir.content:
        # print(type(i))
        print(dir.name, size)

        if type(i) == Dir:
            print('dir')
            size += sizeFinder(i, size)
        elif type(i) == File:
            print('file', i.size)
            size += i.size
    return size


# while cwd.name != '/':
cwd = cwd.parent


print(cwd.name)

s = sizeFinder(cwd, 0)
print(s)
