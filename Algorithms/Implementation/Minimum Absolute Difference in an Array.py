#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    arr.sort()
    Min = arr[1] - arr[0]
    for i in range(len(arr) - 1) :
        diff = abs(arr[i + 1] - arr[i])
        if Min > diff :
            Min = diff
    return Min

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
