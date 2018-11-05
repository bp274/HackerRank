#!/bin/python3

def bfs(n, m, graph, s):
    distance = [-1 for _ in range(n)]
    distance[s] = 0
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = 6 + distance[u]
                    next.append(v)
                elif distance[v] > 6 + distance[u]:
                    distance[v] = 6 + distance[u]
        frontier = next

    return distance

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n, m = map(int, input().strip().split())

        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().strip().split())
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        s = int(input().strip())

        result = bfs(n, m, graph, s - 1)
        for i in range(n):
            if i != s - 1:
                print(result[i], end = ' ')
        print()
