#!/bin/python3

import math

def cdf(x, mean, stanDev):
    return (1 + math.erf((x - mean) / (stanDev * math.sqrt(2)))) / 2

if __name__ == "__main__":
    mean, stanDev = map(int, input().strip().split())
    num1 = int(input().strip())
    num2_3 = int(input().strip())

    result1 = (1 - cdf(num1, mean, stanDev)) * 100
    result2 = (1 - cdf(num2_3, mean, stanDev)) * 100
    result3 = cdf(num2_3, mean, stanDev) * 100

    print(round(result1, 2), round(result2, 2), round(result3, 2), sep = '\n')
