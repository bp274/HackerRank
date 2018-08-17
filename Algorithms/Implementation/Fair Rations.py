#!/bin/python3

def fairRations(B):
    if sum(B) % 2 != 0:
        return "NO"
    else:
        loavesDistributed = 0
        for i in range(len(B) - 1):
            if B[i] % 2 != 0:
                B[i] = B[i] + 1
                B[i + 1] = B[i + 1] + 1
                loavesDistributed = loavesDistributed + 2

        return loavesDistributed


if __name__ == '__main__':
    N = int(input())
    B = list(map(int, input().strip().split()))

    result = fairRations(B)
    print(result)
