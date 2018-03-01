#!/bin/python3

import sys

def viralAdvertising(n) :
    total = 0
    m = 5
    for i in range(n) :
        total = total + (m // 2)
        m = (m // 2) * 3
    return total

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
