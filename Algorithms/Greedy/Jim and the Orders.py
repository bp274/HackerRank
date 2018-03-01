#!/bin/python3

import sys

def jimOrders(orders) :
    total_time = []
    ans = []
    for a, b in orders :
        total_time.append(a + b)
    sorted_time = sorted(total_time)
    for i in range(len(orders)) :
        index = total_time.index(sorted_time[i])
        total_time[index] = ' '
        ans.append(index + 1)
    return ans

if __name__ == "__main__" :
    orders = []
    for _ in range(int(input().strip())) :
        orders.append([int(x) for x in input().strip().split()])
    result = jimOrders(orders)
    print (" ".join(map(str, result)))
