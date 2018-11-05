#!/bin/python3

def union(i, j, parent):
    xRoot = findParent(i, parent)
    yRoot = findParent(j, parent)

    parent[yRoot] = xRoot

def findParent(i, parent):
    if parent[i] != i:
        parent[i] = findParent(parent[i], parent)

    return parent[i]

def kruskalMST(edges):
    totalWeight = 0
    parent = [i for i in range(noOfNodes)]
    for u, v, w in sorted(edges, key = lambda x: x[2]):
        if findParent(u, parent) != findParent(v, parent):
            union(u, v, parent)
            totalWeight += w

    return totalWeight


if __name__ == '__main__':
    noOfNodes, noOfEdges = map(int, input().strip().split())

    edges = []
    for i in range(noOfEdges):
        index1, index2, weight = map(int, input().strip().split())
        edges.append([index1 - 1, index2 - 1, weight])

    result = kruskalMST(edges)
    print(result)
