file = open("inputs/input-2022-13.txt")


def order(first, second):
    fst = first.copy()
    snd = second.copy()
    if first == second:
        return "equal"

    if len(fst) > 0:
        if len(snd) == 0:
            return False
        f = fst[0]
        s = snd[0]
        if type(f) == int:
            if type(s) == int:
                if f < s:
                    return True
                elif f > s:
                    return False
                else:
                    return order(fst[1:], snd[1:])
            elif type(s) == list:
                fst[0] = [f]
                return order(fst, snd)
        elif type(f) == list:
            if type(s) == int:
                snd[0] = [s]
                return order(fst, snd)
            elif type(s) == list:
                if order(f, s) == "equal":
                    return order(fst[1:], snd[1:])
                else:
                    return order(f, s)
    else:
        return True


def minPack(packs):
    min = packs[0]
    for i in packs:
        if not order(min, i):
            min = i
    return min


packs = []
for line in file:
    if line != '\n':
        packs.append(eval(line.strip()))

packs.append([[2]])
packs.append([[6]])

sorted = []
while len(packs) > 0:
    m = minPack(packs)
    packs.remove(m)
    sorted.append(m)


s = 0
e = 0
for i in range(len(sorted)):
    if sorted[i] == [[2]]:
        s = i + 1
    elif sorted[i] == [[6]]:
        e = i + 1


print(s * e)
