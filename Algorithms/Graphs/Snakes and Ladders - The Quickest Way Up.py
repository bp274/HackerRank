#!/bin/python3

def quickestWayUp(position):
    frontier = [0]
    visited = [0 for _ in range(100)]
    rolls = 0
    while frontier:
        next = []
        rolls += 1
        for u in frontier:
            visited[u] = 1
            for v in range(1, 7):
                pos = u + v
                if pos < 100 and visited[pos] == 0:
                    pos = position[u + v]
                    next.append(pos)
                    if pos == 99:
                        return rolls
        frontier = next
    return -1

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):

        position = [i for i in range(100)]

        n = int(input().strip())
        for _ in range(n):
            start, end = map(int, input().strip().split())
            position[start - 1] = end - 1

        m = int(input().strip())
        for _ in range(m):
            start, end = map(int, input().strip().split())
            position[start - 1] = end - 1

        result = quickestWayUp(position)
        print(result)
