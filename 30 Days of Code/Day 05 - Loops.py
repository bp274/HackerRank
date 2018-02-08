#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input())
    for i in range(1, 11) :
        print(n, "x", i, "=", n*i, sep = ' ')
