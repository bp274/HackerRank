#!/bin/python3

def appendAndDelete(s, t, k):
    noOfOperations = 0
    i = 0
    while i < len(s) and i < len(t):
        if s[i] == t[i]:
            i = i + 1
        else:
            break

    if i == len(s) or i == len(t):
        noOfOperations = abs(len(t) - len(s))
    else:
        noOfOperations = len(s) + len(t) - 2 * i

    if noOfOperations == k:
        return "Yes"
    elif noOfOperations > k:
        return "No"
    else:
        uselessOperations = k - noOfOperations
        if uselessOperations % 2 == 0 or uselessOperations > 2 * i:
            return "Yes"
        else:
            return "No"

if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input())

    result = appendAndDelete(s, t, k)
    print(result)
