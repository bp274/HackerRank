#!/bin/python3

import math

def encryption(s):
    s = s.replace(' ', '')
    sqrtL = math.sqrt(len(s))
    rows = math.floor(sqrtL)
    columns = math.ceil(sqrtL)

    ans = ""
    for i in range(columns):
        ans = ans + s[i::columns] + ' '

    return ans

if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)
