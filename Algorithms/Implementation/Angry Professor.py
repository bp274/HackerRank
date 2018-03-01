#!/bin/python3

import sys

def angryProfessor(k, a):
    count = 0
    for x in a :
        if x <= 0 :
            count = count + 1
    if count < k :
        return "YES"
    else :
        return "NO"

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        result = angryProfessor(k, a)
        print(result)
