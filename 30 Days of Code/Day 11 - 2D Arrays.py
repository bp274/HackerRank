#!/bin/python3

import sys

if __name__ == "__main__":
    arr = []
    for _ in range(6) :
        arr.append([int(x) for x in input().split(' ')])
    hsum = []
    for i in range(4) :
        for j in range(4) :
            hsum.append(sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3]))
    print(max(hsum))
