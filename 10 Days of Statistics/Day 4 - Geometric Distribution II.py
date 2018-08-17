#!/bin/python3

from math import pow

if __name__ == "__main__":
    num, den = map(int, input().strip().split())
    inspections = int(input().strip())

    prob = num / den

    result = 0
    for r in range(5):
        result += pow(1 - prob, r) * prob

    print(round(result, 3))
