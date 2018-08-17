#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"

    c1 = c2 = c3 = c4 = 1
    if any(x.isdigit() for x in password):
        c1 = 0
    if any(x.islower() for x in password):
        c2 = 0
    if any(x.isupper() for x in password):
        c3 = 0
    if any(x in special_characters for x in password):
        c4 = 0
    ans = max(6 - n, c1 + c2 + c3 + c4)
    return ans

if __name__ == "__main__":
    n = int(input())
    password = input()
    result = minimumNumber(n, password)
    print(result)
