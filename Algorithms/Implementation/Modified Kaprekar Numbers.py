#!/bin/python3

def isKaprekarNumber(n):
    d = len(str(n))
    n_square = str(n * n)

    r = n_square[len(n_square) - d : len(n_square)]

    l = n_square[0 : len(n_square) - d]
    if l == '':
        l = 0

    if int(r) + int(l) == n:
        return True
    else:
        return False

def kaprekarNumbers(p, q):
    noKaprekarNumber = True
    for i in range(p, q + 1):
        if isKaprekarNumber(i):
            print(i, end = ' ')
            noKaprekarNumber = False

    if noKaprekarNumber:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())
    q = int(input())

    kaprekarNumbers(p, q)
