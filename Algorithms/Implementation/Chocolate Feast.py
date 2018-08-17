#!/bin/python3

def chocolateFeast(n, c, m):
    chocolates = n // c
    wrappers = n // c
    while wrappers >= m:
        chocolates += wrappers // m
        wrappers = (wrappers % m) + (wrappers // m)

    return chocolates

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, c, m = map(int, input().strip().split())

        result = chocolateFeast(n, c, m)
        print(result)
