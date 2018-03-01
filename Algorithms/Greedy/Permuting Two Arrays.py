#!/bin/python3

import sys

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)) :
        if A[i] + B[i] < k :
            return "NO"
    return "YES"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        result = twoArrays(k, A, B)
        print(result)
