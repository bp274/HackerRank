#!/bin/python3

import sys

def countingValleys(n, s) :
    level = 0
    valleys = 0
    for i in s :
        if i == 'U' :
            level = level + 1
        elif i == 'D' :
            level = level - 1
        if level == 0 and i == 'U' :
            valleys = valleys + 1
    return valleys

if __name__ == "__main__" :
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
