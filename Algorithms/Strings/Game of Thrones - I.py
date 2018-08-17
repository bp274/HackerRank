#!/bin/python3

from collections import Counter

def gameOfThrones(s):
    c = Counter(s)

    oddCount = 0
    for x in c:
        if c[x] % 2 != 0:
            oddCount = oddCount + 1

    if oddCount == 1 and len(s) % 2 != 0:
        return "YES"
    elif oddCount == 0 and len(s) % 2 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    s = input().strip()

    result = gameOfThrones(s)
    print(result)
