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
    arr = list(map(int, input().strip().split()))

    mean = getMean(arr)
    standardDeviation = getStandardDeviation(arr, mean)
    print("%.1f" % standardDeviation)
