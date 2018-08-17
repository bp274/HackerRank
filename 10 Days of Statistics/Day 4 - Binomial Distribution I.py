#!/bin/python3

from math import factorial
from math import pow

def combinations(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

if __name__ == "__main__":
    inp = input().strip().split()
    ratio = float(inp[0]) / (float(inp[0]) + 1)
    
    proportion = 0
    for r in range(4):
        proportion = proportion + (combinations(6, r) * pow(ratio, 6 - r) * pow(1 - ratio, r))

    print(round(proportion, 3))
