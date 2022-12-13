import os

os.system("aocd > inputs/input-2022-13.txt")

file = open("inputs/input-2022-13.txt")
# file = open("test.txt")


def compareLists(one, two):  # returns if one comes before two
    while len(one) > 0:
        if len(two) == 0:
            return False

        if one[0] < two[0]:
            return True
        elif one[0] > two[0]:
            return False
        else:
            one.pop()
            two.pop()
    if len(two) > 0:
        return True


def foo(first, second):
    if len(first) > 0:
        if len(second) == 0:
            return False
        f = first[0]
        s = second[0]
        # print(first, second)
        if type(f) == int:
            # print("int")
            if type(s) == int:
                # print('im int too')
                if f < s:
                    return True
                elif f > s:
                    return False
                else:
                    return foo(first[1:], second[1:])
            elif type(s) == list:
                # print('oops')
                first[0] = [f]
                return foo(first, second)
        elif type(f) == list:
            # print('list')
            if type(s) == int:
                # print('oops, but now im an int')
                second[0] = [s]
                return foo(first, second)
            elif type(s) == list:
                # print('im a list too')
                # if foo(f, s) == None:
                #     print('lists equal')
                return foo(f, s)
                # else:
                #     return compareLists(f, s)
    else:
        return True


pairs = []
buff = []
for line in file:
    if line == '\n':
        pairs.append(buff)
        buff = []
    else:
        # buff.append([i for i in line.strip()])
        buff.append(eval(line))
pairs.append(buff)


# for i in pairs:
# print(i)

count = 0
ind = 1
for i in pairs:
    # print(ind)
    if foo(i[0], i[1]):
        count += ind
        # print("true", count)

    ind += 1
print(count)
