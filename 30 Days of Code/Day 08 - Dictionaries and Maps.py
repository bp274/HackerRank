#!/bin/python3

import sys

if __name__ == "__main__":
    d = {}
    for _ in range(int(input())) :
        lst = input().split()
        d[lst[0]] = int(lst[1])
    while True :
        try :
            s = input()
            if s in d :
                print(s, '=', d[s], sep = '')
            else :
                print("Not found")
        except :
            break
