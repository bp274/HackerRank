#!/bin/python3

import sys

def findDigits(n):
    s = str(n)
    count = 0
    for i in s :
        x = int(i)
        if x != 0 and n % x == 0 :
            count = count + 1
    return count

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
