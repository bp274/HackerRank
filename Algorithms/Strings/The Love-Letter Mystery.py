#!/bin/python3

import sys

def theLoveLetterMystery(s):
    n = len(s)
    N = n // 2 if n % 2 == 0 else n // 2 + 1
    count = 0
    for i in range(N):
        count = count + abs(ord(s[i]) - ord(s[n - i - 1]))
    return count

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        result = theLoveLetterMystery(s)
        print(result)
