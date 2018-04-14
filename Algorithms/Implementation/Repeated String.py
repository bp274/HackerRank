#!/bin/python3

import sys

def repeatedString(s, n):
    x = s.count('a')
    l = len(s)
    y = s[:n % l].count('a')
    return x*(n // l) + y

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
