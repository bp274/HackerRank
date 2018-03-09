#!/bin/python3

import sys

if __name__ == "__main__":
    arr = []
    for i in range(int(input())):
        arr.append(input())
    print(*sorted(arr, key = int), sep = '\n')
