#!/bin/python3

def getMedian(arr):
    if len(arr) % 2 != 0:
        median = arr[(len(arr) // 2)]
    else:
        median = (arr[(len(arr) // 2) - 1] + arr[(len(arr) // 2)]) / 2

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
    x = list(map(int, input().strip().split()))
    f = list(map(int, input().strip().split()))

    s = []
    for i in range(n):
        for j in range(f[i]):
            s.append(x[i])

    Q1, Q2, Q3 = getQuartiles(s)
    interQuartileRange = Q3 - Q1
    print("%.1f" % interQuartileRange)
