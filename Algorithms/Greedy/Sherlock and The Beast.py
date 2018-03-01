#!/bin/python3

import sys

def largestDecentNumber(n):
    noOfFives = n - n % 3
    noOfThrees = n % 3
    while noOfFives > 0:            #algo will be better if we check for no. of threes and not for no. of fives
        if noOfThrees % 5 == 0:
            break
        else:
            noOfFives = noOfFives - 3
            noOfThrees = noOfThrees + 3
    if noOfThrees % 5 != 0:
        return -1
    s = '5'*noOfFives + '3'*noOfThrees
    return s

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        result = largestDecentNumber(n)
        print(result)
