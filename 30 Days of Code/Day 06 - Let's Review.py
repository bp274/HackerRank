#!/bin/python3

import sys

if __name__ == "__main__":
    for _ in range(int(input())) :
        s = input()
        for i in range(0, len(s), 2) :
            print(s[i], end = '')
        print(end = ' ')
        for i in range(1, len(s), 2) :
            print(s[i], end = '')
        print()
