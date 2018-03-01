#!/bin/python3

import sys

def jumpingOnClouds(c, k):
    return 100 - sum(1 + 2*c[i] for i in range(0, n, k))

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    c = list(map(int, input().strip().split()))
    result = jumpingOnClouds(c, k)
    print(result)
