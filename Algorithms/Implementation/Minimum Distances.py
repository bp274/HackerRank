#!/bin/python3

import sys

def minimumDistances(a):
    d = {}
    n = len(a)
    minDiff = n
    for i in range(n):
        if a[i] in d:
            minDiff = min(i - d[a[i]], minDiff)
            d[a[i]] = i
            if minDiff == 1:
                break
        else:
            d[a[i]] = i
    return minDiff if minDiff < n else -1

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    result = minimumDistances(a)
    print(result)
