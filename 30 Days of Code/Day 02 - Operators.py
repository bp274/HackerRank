#!/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    total_cost = int(round(meal_cost + tip_percent*(meal_cost / 100) + tax_percent*(meal_cost / 100)))
    print("The total meal cost is " + str(total_cost) + " dollars.")
