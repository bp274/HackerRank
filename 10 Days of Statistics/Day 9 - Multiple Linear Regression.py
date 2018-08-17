#!/bin/python3

from sklearn import linear_model

if __name__ == "__main__":
    m, n = map(int, input().strip().split())

    f = []
    y = []
    for _ in range(n):
        values = list(map(float, input().strip().split()))
        f.append(values[:-1])
        y.append(values[-1])

    lm = linear_model.LinearRegression()
    lm.fit(f, y)
    a = lm.intercept_
    b = lm.coef_

    q = int(input().strip())
    for _ in range(q):
        f = list(map(float, input().strip().split()))

        y = a + sum(f[i] * b[i] for i in range(m))
        print(y)
