#!/bin/python3

import sys

def cutTheSticks(arr):
    arr.sort()
    ans = []
    while arr:
        l = []
        count = 0
        for x in arr:
            count = count + 1
            if x > arr[0]:
                l.append(x - arr[0])
        arr = l
        ans.append(count)
    return ans

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = cutTheSticks(arr)
    print ("\n".join(map(str, result)))
