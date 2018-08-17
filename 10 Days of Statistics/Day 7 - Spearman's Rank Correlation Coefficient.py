#!/bin/python3

import math

def spearmanRankCorrelationCoefficient(rankX, rankY):
    Rxy = 0
    n = len(rankX)
    for i in range(n):
        Rxy += math.pow((rankX[i] - rankY[i]), 2)

    Rxy = 1 - ((6 * Rxy) / (n * (math.pow(n, 2) - 1)))

    return Rxy

def getRank(arr):
    rank = {}
    i = 1
    for value in sorted(set(arr)):
        rank[value] = i
        i = i + 1

    rank = [rank[value] for value in arr]
    return rank

if __name__ == "__main__":
    n = int(input().strip())
    X = list(map(float, input().strip().split()))
    Y = list(map(float, input().strip().split()))

    rankX = getRank(X)
    rankY = getRank(Y)

    Rxy = spearmanRankCorrelationCoefficient(rankX, rankY)
    print(round(Rxy, 3))
