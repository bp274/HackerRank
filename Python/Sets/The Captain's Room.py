n = int(input())
l = list(map(int, input().split()))
s = set(l)
print((n*sum(s) - sum(l)) // (n - 1))
