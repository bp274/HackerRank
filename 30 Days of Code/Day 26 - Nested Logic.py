#!/bin/python3

import sys

if __name__ == "__main__":
    d2, m2, y2 = map(int, input().split())
    d1, m1, y1 = map(int, input().split())
    if y2 < y1 or (y2 == y1 and m2 < m1) or (y2 == y1 and m2 == m1 and d2 <= d1) :
        print(0)
    elif y2 > y1 :
        print(10000)
    elif m2 > m1 :
        print(500 * (m2 - m1))
    else :
        print(15 * (d2 - d1))
