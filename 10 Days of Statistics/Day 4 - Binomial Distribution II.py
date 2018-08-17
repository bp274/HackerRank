#!/bin/python3

from math import factorial
from math import pow

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

if __name__ == "__main__":
    prob, pistons = map(int, input().strip().split())
    prob = prob / 100

    max2Rejects = 0
    for r in range(3):
        max2Rejects += (combinations(pistons, r) * pow(prob, r) * pow(1 - prob, pistons - r))

    min2Rejects = 0
    for r in range(2, 11):
        min2Rejects += (combinations(pistons, r) * pow(prob, r) * pow(1 - prob, pistons - r))

    print(round(max2Rejects, 3), round(min2Rejects, 3), sep = '\n')
