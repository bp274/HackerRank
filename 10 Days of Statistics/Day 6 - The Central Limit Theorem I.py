#!/bin/python3

import math

def cdf(x, mean, stanDev):
    return (1 + math.erf((x - mean) / (stanDev * math.sqrt(2)))) / 2

if __name__ == "__main__":
    maxWeight = float(input().strip())
    num = float(input().strip())
    mean = float(input().strip())
    stanDev = float(input().strip())

    newMean = num * mean
    newStanDev = math.sqrt(num) * stanDev

    result = cdf(maxWeight, newMean, newStanDev)
    print(round(result, 4))
