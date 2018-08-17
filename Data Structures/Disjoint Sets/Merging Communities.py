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

if __name__ == "__main__":
    n, q = map(int, input().strip().split())

    parent = [i for i in range(n)]
    count = [1 for _ in range(n)]

    for _ in range(q):
        query = input().strip().split()
        if query[0] == 'M':
            i, j = int(query[1]), int(query[2])
            union(i - 1, j - 1, parent, count)
        elif query[0] == 'Q':
            i = int(query[1])
            iParent = find(i - 1, parent)
            print(count[iParent])
