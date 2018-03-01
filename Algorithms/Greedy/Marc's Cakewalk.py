#!/bin/python3

import sys

def marcsCakewalk(calorie, n) :
    miles = 0
    for i in sorted(calorie) :
        n = n - 1
        miles = miles + ((2**n) * i)
    return miles

if __name__ == "__main__" :
    n = int(input().strip())
    calorie = list(map(int, input().strip().split()))
    result = marcsCakewalk(calorie, n)
    print(result)
