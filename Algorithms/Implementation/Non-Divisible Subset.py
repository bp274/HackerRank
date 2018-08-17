#!/bin/python3

def nonDivisibleSubset(k, S):
    rem = [0] * k
    for x in S:
        rem[x % k] += 1

    maxSize = 1 if rem[0] > 0 else 0
    for i in range(1, k // 2 + 1):
        maxSize += max(rem[i], rem[k - i])

    if k % 2 == 0 and rem[k // 2] > 0:
        maxSize -= rem[k // 2] - 1

    return maxSize

if __name__ == '__main__':
    n, k = map(int, input().strip().split())

    S = list(map(int, input().strip().split()))

    result = nonDivisibleSubset(k, S)
    print(result)
