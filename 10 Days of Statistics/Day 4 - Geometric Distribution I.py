#!/bin/python3

from math import pow

if __name__ == "__main__":
    num, den = map(int, input().strip().split())
    firstDefect = int(input().strip())

    prob = num / den

    result = pow(1 - prob, 4) * prob
    print(round(result, 3))
