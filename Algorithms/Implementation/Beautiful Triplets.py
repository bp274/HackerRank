#!/bin/python3

def beautifulTriplets(d, arr):
    numberOfBeautifulTriplets = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            tripletFound = False
            if arr[j] == arr[i] + d:
                for k in range(j + 1, len(arr)):
                    if arr[k] == arr[j] + d:
                        numberOfBeautifulTriplets = numberOfBeautifulTriplets + 1
                        tripletFound = True
                        break
            if tripletFound:
                break

    return numberOfBeautifulTriplets

if __name__ == '__main__':
    n, d = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    result = beautifulTriplets(d, arr)
    print(result)
