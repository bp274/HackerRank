#!/bin/python3

import sys
import math

if __name__ == "__main__":
    for _ in range(int(input())) :
        n = int(input())
        isPrime = True
        if n == 1 :
            isPrime = False
        elif n <= 3 :
            isPrime = True
        elif n % 2 == 0 :
            isPrime = False
        else :
            for i in range(3, int(math.sqrt(n)) + 1, 2) :
                if n % i == 0 :
                    isPrime = False
                    break
        print("Prime" if isPrime else "Not prime")
