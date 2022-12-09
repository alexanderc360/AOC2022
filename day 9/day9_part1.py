import os

os.system("aocd > inputs/input-2022-9.txt")

file = open("inputs/input-2022-9.txt")

steps = []
for line in file:
    steps.append(line.split())

head = [0, 0]  # [x,y]
tail = [0, 0]  # [x,y]

tracker = []


for i in steps:
    n = int(i[1])

    # moves head by 1
    for j in range(n):
        if i[0] == 'R':
            head[0] += 1
        elif i[0] == 'L':
            head[0] -= 1
        elif i[0] == 'U':
            head[1] += 1
        elif i[0] == 'D':
            head[1] -= 1
        # updates tail
        # if the tail is not touching the head
        if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
            if head[0] == tail[0] or head[1] == tail[1]:  # both in same col or row
                if head[0] - tail[0] == 2:  # right
                    tail[0] += 1
                elif head[0] - tail[0] == -2:  # left
                    tail[0] -= 1
                elif head[1] - tail[1] == 2:  # up
                    tail[1] += 1
                elif head[1] - tail[1] == -2:  # down
                    tail[1] -= 1
            else:
                if head[0] > tail[0] and head[1] > tail[1]:
                    tail[0] += 1
                    tail[1] += 1
                elif head[0] > tail[0] and head[1] < tail[1]:
                    tail[0] += 1
                    tail[1] -= 1
                elif head[0] < tail[0] and head[1] < tail[1]:
                    tail[0] -= 1
                    tail[1] -= 1
                elif head[0] < tail[0] and head[1] > tail[1]:
                    tail[0] -= 1
                    tail[1] += 1

        tracker.append(tuple(tail.copy()))


l = set(tracker)
print(len(l))
