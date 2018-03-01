#!/bin/python3

import sys

def toys(w) :
    w.sort()
    cost = 1
    x = w[0]
    for y in w :
        if y - x > 4 :
            x = y
            cost = cost + 1
    return cost

if __name__ == "__main__":
    n = int(input().strip())
    w = list(map(int, input().strip().split()))
    result = toys(w)
    print(result)
