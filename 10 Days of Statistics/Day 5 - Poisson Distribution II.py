#!/bin/python3

if __name__ == "__main__":
    meanA, meanB = map(float, input().strip().split())

    expA = 160 + 40 * (meanA + meanA * meanA)
    expB = 128 + 40 * (meanB + meanB * meanB)

    print(round(expA, 3), round(expB, 3), sep = '\n')
