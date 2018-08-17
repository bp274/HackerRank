#!/bin/python3

import math

def getMean(arr):
    return sum(arr) / len(arr)

def getStandardDeviation(arr, mean):
    variance = 0
    for x in arr:
        variance = variance + math.pow(x - mean, 2)
    variance = variance / n

    standardDeviation = math.sqrt(variance)
    return standardDeviation

if __name__ == "__main__":
    n = int(input().strip())
    X = list(map(float, input().strip().split()))
    Y = list(map(float, input().strip().split()))

    meanX = getMean(X)
    stanDevX = getStandardDeviation(X, meanX)

    meanY = getMean(Y)
    stanDevY = getStandardDeviation(Y, meanY)

    pearsonCorrelationCoefficient = 0
    for i in range(n):
        pearsonCorrelationCoefficient += (X[i] - meanX) * (Y[i] - meanY)
    pearsonCorrelationCoefficient = pearsonCorrelationCoefficient / (n * stanDevX * stanDevY)

    print(round(pearsonCorrelationCoefficient, 3))
