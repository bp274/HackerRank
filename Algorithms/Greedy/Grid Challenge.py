#!/bin/python3

import sys

def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(list(grid[i]))
    grid = list(map(list, zip(*grid)))
    return "YES" if all(grid[i][j] <= grid[i][j + 1] for j in range(len(grid) - 1) for i in range(len(grid))) else "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []
        for i in range(n) :
            grid.append(str(input().strip()))
        result = gridChallenge(grid)
        print(result)
