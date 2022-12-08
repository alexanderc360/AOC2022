file = open("inputs/input-2022-7.txt")


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

cwd = Dir(None, None)

i = 0
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

    i += 1


def sizeFinder(dir):
    size = 0
    for i in dir.content:
        if type(i) == File:
            size += i.size
        elif type(i) == Dir:
            size += sizeFinder(i)
    return size


def spaceFinder(dir, need, min):
    for i in dir.content:
        if type(i) == Dir:
            s = sizeFinder(i)
            if s >= need:
                if min == 0 or s < min:
                    min = s
            min = spaceFinder(i, need, min)
    return min


while cwd.name != '/':
    cwd = cwd.parent

totalSpace = 70000000

unused = totalSpace - sizeFinder(cwd)
need = 30000000 - unused


print(spaceFinder(cwd, need, 0))
