#!/bin/python3

import math

def getMean(arr):
    return sum(arr) / len(arr)

def getStandardDeviation(arr, mean):
    variance = 0
    for x in arr:
        variance = variance + math.pow(x - mean, 2)
    variance = variance / len(arr)

    standardDeviation = math.sqrt(variance)
    return standardDeviation

def getPearsonCorrelationCoefficient(X, Y):
    n = len(X)
    meanX = getMean(X)
    meanY = getMean(y)
    pearsonCorrelationCoefficient = 0
    for i in range(n):
        pearsonCorrelationCoefficient += (X[i] - meanX) * (Y[i] - meanY)
    pearsonCorrelationCoefficient = pearsonCorrelationCoefficient / (n * stanDevX * stanDevY)

    return pearsonCorrelationCoefficient

if __name__ == "__main__":
    x = []
    y = []
    for i in range(5):
        marks = input().strip().split()
        x.append(int(marks[0]))
        y.append(int(marks[1]))

    meanY = getMean(y)
    stanDevY = getStandardDeviation(y, meanY)

    meanX = getMean(x)
    stanDevX = getStandardDeviation(x, meanX)

    pearsonCorrelationCoefficient = getPearsonCorrelationCoefficient(x, y)

    b = (pearsonCorrelationCoefficient * stanDevY) / stanDevX
    a = meanY - b * meanX

    expectedY = a + b * 80
    print(round(expectedY, 3))
