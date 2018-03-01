#!/bin/python3

import sys

def beautifulDays(i, j, k) :
    beautiful_days = 0
    for x in range(i, j + 1) :
        if abs(x - int(str(x)[::-1])) % k == 0 :
            beautiful_days = beautiful_days + 1
    return beautiful_days

if __name__ == "__main__" :
    i, j, k = map(int, input().strip().split())
    result = beautifulDays(i, j, k)
    print(result)
