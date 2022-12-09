file = open("inputs/input-2022-9.txt")
# file = open("test.txt")

steps = []
for line in file:
    steps.append(line.split())


def touching(head, tail):
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
    return tail


snake = [[0, 0] for i in range(10)]  # [x,y]

tracker = []


head = snake[0]
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

        # makes sure the snake parts are touching
        for k in range(len(snake)-1):
            snake[k+1] = touching(snake[k], snake[k+1])

        tracker.append(tuple(snake[-1].copy()))


l = set(tracker)
print(len(l))
