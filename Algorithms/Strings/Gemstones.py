#!/bin/python3

def gemstones(arr):
    setList = [set(x) for x in arr]
    gems = set.intersection(*(setList))

    return len(gems)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
    print(result)
