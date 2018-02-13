#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    swaps = 0
    for i in range(n) :
        numberOfSwaps = 0
        for j in range(n - 1 - i) :
            if a[j] > a[j + 1] :
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps = numberOfSwaps + 1
        swaps = swaps + numberOfSwaps
        if numberOfSwaps == 0 :
            break
    print("Array is sorted in %i swaps." % swaps)
    print("First Element: %i" % a[0])
    print("Last Element: %i" % a[n - 1])
