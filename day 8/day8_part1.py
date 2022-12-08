import os

os.system("aocd > inputs/input-2022-8.txt")

file = open("inputs/input-2022-8.txt")


def visible(row, col, grid):
    val = grid[row][col]

    if row == 0 or row == len(grid)-1:
        return True
    if col == 0 or col == len(grid[0])-1:
        return True

    # print(grid[row])

    # left
    vis = True
    for i in range(col):
        if grid[row][i] >= val:
            vis = False
    if vis:
        return True

    # right
    vis = True
    for i in range(col+1, len(grid[0]), 1):
        if grid[row][i] >= val:
            vis = False
    if vis:
        return True

    # up
    vis = True
    for i in range(row):
        if grid[i][col] >= val:
            vis = False
    if vis:
        return True

    # down
    vis = True
    for i in range(row+1, len(grid), 1):
        if grid[i][col] >= val:
            vis = False
    if vis:
        return True


grid = []
for line in file:
    buff = []
    for i in line.strip():
        buff.append(i)
    grid.append(buff)

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visible(i, j, grid):
            count += 1

print(count)
