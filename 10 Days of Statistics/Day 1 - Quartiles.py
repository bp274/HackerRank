#!/bin/python3

def getMedian(arr):
    if len(arr) % 2 != 0:
        median = arr[(len(arr) // 2)]
    else:
        median = (arr[(len(arr) // 2) - 1] + arr[(len(arr) // 2)]) // 2

    return median

def getQuartiles(lst):
    lst.sort()
    q1 = getMedian(lst[:len(lst) // 2])
    q2 = getMedian(lst)
    if len(lst) % 2 == 0:
        q3 = getMedian(lst[len(lst) // 2:])
    else:
        q3 = getMedian(lst[(len(lst) // 2) + 1:])

    return q1, q2, q3

if __name__ == "__main__":
    n = int(input().strip())
    lst = list(map(int, input().strip().split()))

    Q1, Q2, Q3 = getQuartiles(lst)
    print(Q1, Q2, Q3, sep = '\n')
