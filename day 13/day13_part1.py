import os

# os.system("aocd > inputs/input-2022-13.txt")

file = open("inputs/input-2022-13.txt")


def foo(first, second):
    if first == second:
        return "equal"

    if len(first) > 0:
        if len(second) == 0:
            return False
        f = first[0]
        s = second[0]
        if type(f) == int:
            if type(s) == int:
                if f < s:
                    return True
                elif f > s:
                    return False
                else:
                    return foo(first[1:], second[1:])
            elif type(s) == list:
                first[0] = [f]
                return foo(first, second)
        elif type(f) == list:
            if type(s) == int:
                second[0] = [s]
                return foo(first, second)
            elif type(s) == list:
                if foo(f, s) == "equal":
                    return foo(first[1:], second[1:])
                else:
                    return foo(f, s)
    else:
        return True


pairs = []
buff = []
for line in file:
    if line == '\n':
        pairs.append(buff)
        buff = []
    else:
        buff.append(eval(line))
pairs.append(buff)


count = 0
ind = 1
for i in pairs:
    if foo(i[0], i[1]):
        count += ind
    ind += 1


print(count)
