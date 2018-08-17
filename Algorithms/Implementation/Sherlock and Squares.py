#!/bin/python3

import math

def squares(a, b):
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)

    lowerLimit = math.ceil(sqrt_a)
    upperLimit = math.floor(sqrt_b)

    count = 0
    for i in range(lowerLimit, upperLimit + 1):
        count = count + 1
    return count

if __name__ == '__main__':
    for t in range(int(input())):
        a, b = map(int, input().strip().split())
        result = squares(a, b)
        print(result)
