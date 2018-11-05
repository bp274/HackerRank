#!/bin/python3

def getWeight(graph, weight, currNode, prevNode):
    weight[currNode] = 1
    for nextNode in graph[currNode]:
        if nextNode != prevNode:
            weight[currNode] += getWeight(graph, weight, nextNode, currNode)

    return weight[currNode]

if __name__ == '__main__':
    noOfNodes, noOfEdges = map(int, input().strip().split())

    graph = [[] for _ in range(noOfNodes)]
    for i in range(noOfEdges):
        u, v = map(int, input().strip().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    weight = [0 for _ in range(noOfNodes)]
    getWeight(graph, weight, 0, None)

    count = 0
    for x in weight:
        if x % 2 == 0:
            count += 1
    print(count - 1)
