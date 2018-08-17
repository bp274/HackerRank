#!/bin/python3

import sys

def getRanks(scores):
    ranks = []
    rank = 0
    score = -1
    for i in range(len(scores)):
        if scores[i] != score:
            score = scores[i]
            rank = rank + 1
        ranks.append(rank)
    return ranks

def climbingLeaderboard(scores, alice):
    scores.append(-1)
    ranks = getRanks(scores)
    i = len(scores) - 1
    for x in alice:
        while i >= 0 and x >= scores[i]:
            i = i - 1
        if i >= 0:
            print(ranks[i] + 1)
        else:
            print(1)


if __name__ == '__main__':
    n = int(input().strip())
    scores = [int(x) for x in input().strip().split()]
    m = int(input().strip())
    alice = [int(x) for x in input().strip().split()]
    climbingLeaderboard(scores, alice)
