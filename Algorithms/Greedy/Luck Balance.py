#!/bin/python3

import sys

def luckBalance(n, k, contests) :
    luck = 0
    counter = 0
    for i in contests :
        if i[1] == 1 :
            counter = counter + 1
    for contest in sorted(contests) :
        if contest[1] == 0 :
            luck = luck + contest[0]
        else :
            if counter <= k :
                luck = luck + contest[0]
            else :
                luck = luck - contest[0]
            counter = counter - 1
    return luck

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    contests = []
    for contests_i in range(n):
        contests.append([int(x) for x in input().strip().split()])
    result = luckBalance(n, k, contests)
    print(result)
