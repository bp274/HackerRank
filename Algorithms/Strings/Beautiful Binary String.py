#!/bin/python3

import sys

def beautifulBinaryString(b):
    return b.count('010')

if __name__ == "__main__":
    n = int(input().strip())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result)
