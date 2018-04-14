#!/bin/python3

import sys
from collections import Counter

def equalizeArray(arr):
    c = Counter(arr)
    return len(arr) - max(c[x] for x in arr)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = equalizeArray(arr)
    print(result)
