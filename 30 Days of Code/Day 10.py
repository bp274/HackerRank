#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input())
    maximum = cons = 0
    while n > 0 :
        if n % 2 == 1 :
            cons = cons + 1
        else :
            if cons > maximum :
                maximum = cons
            cons = 0
        n = n // 2
    if cons > maximum :
        maximum = cons
    print(maximum)
