#!/bin/python3

import sys

def circularArrayRotation(a, m, k):
    l = []
    N = len(a)
    k = k % N
    for x in m:
        index = x - k if x >= k else x - k + N
        l.append(a[index])
    return l

if __name__ == "__main__":
    n, k, q = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    m = []
    for _ in range(q):
        m.append(int(input().strip()))
    result = circularArrayRotation(a, m, k)
    print ("\n".join(map(str, result)))
