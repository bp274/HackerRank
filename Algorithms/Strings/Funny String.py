#!/bin/python3

import sys

def funnyString(s):
    for i in range(1, len(s)) :
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[-i - 1]) - ord(s[-i])) :
            return "Not Funny"
    return "Funny"

if __name__ == "__main__":
    for _ in range(int(input())) :
        print(funnyString(input()))
