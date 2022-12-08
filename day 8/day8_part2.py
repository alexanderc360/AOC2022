file = open("inputs/input-2022-8.txt")


def score(row, col, grid):
    val = grid[row][col]

    # left
    l = 0
    for i in range(col-1, -1, -1):
        l += 1
        if grid[row][i] >= val:
            break

    # right
    r = 0
    for i in range(col+1, len(grid[0]), 1):
        r += 1
        if grid[row][i] >= val:
            break

    # up
    u = 0
    for i in range(row-1, -1, -1):
        u += 1
        if grid[i][col] >= val:
            break

    # down
    d = 0
    for i in range(row+1, len(grid), 1):
        d += 1
        if grid[i][col] >= val:
            break

    return l * r * u * d


grid = []
for line in file:
    buff = []
    for i in line.strip():
        buff.append(i)
    grid.append(buff)

max = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        s = score(i, j, grid)
        if s > max:
            max = s

print(max)
