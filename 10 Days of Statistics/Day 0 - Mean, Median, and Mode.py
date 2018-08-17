#!/bin/python3

def getMean(arr):
    mean = sum(arr) / n
    return mean

def getMedian(arr):
    arr.sort()
    if len(arr) % 2 != 0:
        median = arr[(len(arr) // 2)]
    else:
        median = (arr[(len(arr) // 2) - 1] + arr[(len(arr) // 2)]) / 2

    return median

def getMode(arr):
    arr.sort()
    maxCount = 1
    mode = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count = count + 1
        else:
            count = 1
        if count > maxCount:
            maxCount = count
            mode = arr[i]

    return mode

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    mean = getMean(arr)
    median = getMedian(arr)
    mode = getMode(arr)
    print("%.1f\n%.1f\n%.1f" % (mean, median, mode))
