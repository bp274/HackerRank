#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input())
    if n % 2 == 1 :
        print("Weird")
    elif n < 5 :
        print("Not Weird")
    elif n <= 20 :
        print("Weird")
    else :
        print("Not Weird")
