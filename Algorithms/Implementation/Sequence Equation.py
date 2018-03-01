#!/bin/python3

import sys

def permutationEquation(p):
    l = []
    for x in range(1, len(p) + 1) :
        for y in range(0, len(p)) :
            if x == p[p[y] - 1] :
                l.append(y + 1)
    return l

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split()))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))
