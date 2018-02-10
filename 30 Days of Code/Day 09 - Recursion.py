#!/bin/python3

import sys

def factorial(n):
    if n <= 2 :
        return n
    return n*factorial(n - 1)

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
