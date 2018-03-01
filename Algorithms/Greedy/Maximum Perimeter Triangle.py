#!/bin/python3

import sys

def maximumPerimeterTriangle(l):
    l.sort(reverse = True)
    for i in range(len(l) - 2):
        if l[i] < l[i + 1] + l[i + 2]:
            return [l[i + 2], l[i + 1], l[i]]
    return [-1]

if __name__ == "__main__":
    n = int(input().strip())
    l = list(map(int, input().strip().split()))
    result = maximumPerimeterTriangle(l)
    print (" ".join(map(str, result)))
