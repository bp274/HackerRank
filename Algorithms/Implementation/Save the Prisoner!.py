#!/bin/python3

import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    if (m + s - 1) % n == 0:
        return n
    else:
        return (m + s - 1) % n

if __name__ == '__main__':
    for t in range(int(input().strip())):
        n, m, s = map(int, input().strip().split())
        result = saveThePrisoner(n, m, s)
        print(result)
