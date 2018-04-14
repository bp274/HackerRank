#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    pay = (sum(ar) - ar[k]) // 2
    if b == pay :
        return "Bon Appetit"
    else :
        return b - pay
        
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    ar = list(map(int, input().strip().split(' ')))
    b = int(input().strip())
    result = bonAppetit(n, k, b, ar)
    print(result)
