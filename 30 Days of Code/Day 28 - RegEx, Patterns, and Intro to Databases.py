#!/bin/python3

import sys
import re

if __name__ == "__main__":
    l = []
    for _ in range(int(input())) :
        l.append(input().split())
    l.sort()
    for x in l :
        if re.search('@gmail.com', x[1]) :
            print(x[0])
