#!/bin/python3

def cavityMap(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] > grid[i - 1][j] and grid[i][j] > grid[i + 1][j] and grid[i][j] > grid[i][j + 1] and grid[i][j] > grid[i][j - 1]:
                grid[i][j] = 'X'

    for i in range(len(grid)):
        print("".join(str(x) for x in grid[i]))

if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = list(input())
        grid.append(grid_item)

    cavityMap(grid)
