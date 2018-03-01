#!/bin/python3

import sys

def catAndMouse(x, y, z):
    a = abs(x - z)
    b = abs(y - z)
    if a == b :
        return "Mouse C"
    if a < b :
        return "Cat A"
    return "Cat B"

if __name__ == "__main__":
    for a0 in range(int(input().strip())) :
        x, y, z = map(int, input().strip().split())
        result = catAndMouse(x, y, z)
        print(result)
