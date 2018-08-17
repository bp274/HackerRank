#!/bin/python3

def getMean(x, w):
    total = 0
    for i in range(len(x)):
        total = total + x[i] * w[i]
    mean = total / sum(w)

    return mean

if __name__ == "__main__":
    n = int(input().strip())
    x = list(map(int, input().strip().split()))
    w = list(map(int, input().strip().split()))

    mean = getMean(x, w)
    print("%.1f" % mean)
