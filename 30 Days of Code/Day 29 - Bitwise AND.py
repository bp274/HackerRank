#!/bin/python3

import sys

if __name__ == "__main__":
    for _ in range(int(input())) :
        n, k = map(int, input().split())
        if k - 1 | k <= n :
            print(k - 1)
        else :
            print(k - 2)
