#!/bin/python3

import sys

def getMinimumCost(n, k, c) :
    cost = 0
    c.sort()
    for i in range(n) :
        cost = cost + (1 + i // k) * c[n - i - 1]
    return cost


if __name__ == "__main__" :
    n, k = map(int, input().strip().split())
    c = list(map(int, input().strip().split()))
    minimumCost = getMinimumCost(n, k, c)
    print(minimumCost)
