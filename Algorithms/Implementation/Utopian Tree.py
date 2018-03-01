#!/bin/python3

import sys

def utopianTree(n):
    height = 1
    for i in range(1, n + 1) :
        if i % 2 == 1 :
            height = 2 * height
        else :
            height = height + 1
    return height

if __name__ == "__main__":
    for a0 in range(int(input().strip())) :
        result = utopianTree(int(input().strip()))
        print(result)
