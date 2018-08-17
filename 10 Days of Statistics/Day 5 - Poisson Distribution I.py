#!/bin/python3

from math import exp
from math import factorial
from math import pow

if __name__ == "__main__":
    mean = float(input().strip())
    value = int(input().strip())

    prob = (pow(mean, value) * exp(-mean)) / factorial(value)

    print(round(prob, 3))
