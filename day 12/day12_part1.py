import os

# os.system("aocd > inputs/input-2022-12.txt")

file = open("inputs/input-2022-12.txt")


def pathSearch(cur, grid, status):
    val = grid[cur[0]][cur[1]]
    steps = status[cur[0]][cur[1]] + 1
    if cur[0] != len(grid)-1:
        if grid[cur[0]+1][cur[1]] <= val+1:  # down
            if status[cur[0]+1][cur[1]] == -1 or status[cur[0]+1][cur[1]] > steps:
                status[cur[0]+1][cur[1]] = steps

    if cur[0] != 0:
        if grid[cur[0]-1][cur[1]] <= val+1:  # up
            if status[cur[0]-1][cur[1]] == -1 or status[cur[0]-1][cur[1]] > steps:
                status[cur[0]-1][cur[1]] = steps

    if cur[1] != len(grid[0])-1:
        if grid[cur[0]][cur[1]+1] <= val+1:  # right
            if status[cur[0]][cur[1]+1] == -1 or status[cur[0]][cur[1]+1] > steps:
                status[cur[0]][cur[1]+1] = steps

    if cur[1] != 0:
        if grid[cur[0]][cur[1]-1] <= val+1:  # left
            if status[cur[0]][cur[1]-1] == -1 or status[cur[0]][cur[1]-1] > steps:
                status[cur[0]][cur[1]-1] = steps

    return status


start = []
end = []

grid = []
for line in file:
    buff = []
    for i in line.strip():
        if i == 'S':
            start.append(len(grid))
            start.append(len(buff))
            buff.append(ord('a')-97)
        elif i == 'E':
            end.append(len(grid))
            end.append(len(buff))
            buff.append(ord('z')-97)
        else:
            buff.append(ord(i)-97)
    grid.append(buff)


status = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
status[start[0]][start[1]] = 0

i = 0
while status[end[0]][end[1]] < 0:
    for j in range(len(grid)):
        for k in range(len(grid[0])):
            if status[j][k] == i:
                status = pathSearch([j, k], grid, status)
    i += 1

print('answer', status[end[0]][end[1]])
