#!/bin/python3

import math

if __name__ == "__main__":
    sampleSize = float(input().strip())
    mean = float(input().strip())
    stanDev = float(input().strip())
    distPercentage = float(input().strip())
    z = float(input().strip())

    marginOfError = z * (stanDev / math.sqrt(sampleSize))

    A = mean - marginOfError
    B = mean + marginOfError
    print(round(A, 2), round(B, 2), sep = '\n')
