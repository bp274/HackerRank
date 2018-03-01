#!/bin/python3

import sys

def maximumToys(prices, k):
    toys = 0
    for i in sorted(prices) :
        if k - i > 0 :
            toys = toys + 1
            k = k - i
        else :
            break ;
    return toys

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    prices = list(map(int, input().strip().split()))
    result = maximumToys(prices, k)
    print(result)
