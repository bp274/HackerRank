#!/bin/python3

def union(i, j, parent, count):
    xRoot = find(i, parent)
    yRoot = find(j, parent)

    parent[yRoot] = xRoot
    if xRoot != yRoot:
        count[xRoot] = count[xRoot] + count[yRoot]
        count[yRoot] = 0

def find(i, parent):
    if parent[i] != i:
        parent[i] = find(parent[i], parent)

    return parent[i]

def findMinMax(count):
    minimum = len(count)
    maximum = 0
    for x in count:
        if x > 1 and x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    n = int(input())

    parent = [i for i in range(2 * n)]
    count = [1 for _ in range(2 * n)]

    for i in range(n):
        Gi, Bi = map(int, input().strip().split())
        union(Gi - 1, Bi - 1, parent, count)

    result = findMinMax(count)
    print(result[0], result[1], sep = ' ')
