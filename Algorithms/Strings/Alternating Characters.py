#!/bin/python3

import sys

def alternatingCharacters(s):
    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 1:]
            count = count + 1
            i = i - 1
        i = i + 1
    return count
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = alternatingCharacters(s)
        print(result)
