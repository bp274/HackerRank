#!/bin/python3

def taumBday(b, w, bc, wc, z):
    if bc + z < wc:
        return b * bc + w * (bc + z)
    elif wc + z < bc:
        return w * wc + b * (wc + z)
    else:
        return b * bc + w * wc

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        b, w = map(int, input().strip().split())
        bc, wc, z = map(int, input().strip().split())

        result = taumBday(b, w, bc, wc, z)
        print(result)
