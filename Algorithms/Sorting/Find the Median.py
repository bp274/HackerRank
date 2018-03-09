#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(sorted(ar)[n // 2])
