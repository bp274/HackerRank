#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s) :
    cost = -1
    i = j = 0
    while i < len(keyboards) :
        while j < len(drives) :
            if s < keyboards[i] + drives[j] :
                break
            if cost < keyboards[i] + drives[j] :
                cost = keyboards[i] + drives[j]
            j = j + 1
        i = i + 1
    return cost

if __name__ == "__main__" :
    s, n, m = map(int, input().split())
    keyboards = [int(x) for x in input().split()]
    drives = [int(x) for x in input().split()]
    moneySpent = getMoneySpent(sorted(keyboards, reverse = True), sorted(drives), s)
    print(moneySpent)
