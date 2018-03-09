#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = []
    mini = a[1] - a[0]
    for i in range(n - 1) :
        if (a[i + 1] - a[i]) <= mini :
            if (a[i + 1] - a[i]) < mini :
                l = []
                mini = a[i + 1] - a[i]
            l.append(a[i])
            l.append(a[i + 1])

    for i in range(0, len(l), 2) :
        print(l[i], l[i + 1], sep = ' ' , end = ' ')
