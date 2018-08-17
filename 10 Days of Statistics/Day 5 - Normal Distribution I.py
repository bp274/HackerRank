#!/bin/python3

import math

def cdf(x, mean, stanDev):
    return (1 + math.erf((x - mean) / (stanDev * math.sqrt(2)))) / 2

if __name__ == "__main__":
    mean, stanDev = map(float, input().strip().split())
    part1 = float(input().strip())
    part2Lower, part2Upper = map(float, input().strip().split())

    result1 = cdf(part1, mean, stanDev)
    result2 = cdf(part2Upper, mean, stanDev) - cdf(part2Lower, mean, stanDev)

    print(round(result1, 3), round(result2, 3), sep = '\n')
