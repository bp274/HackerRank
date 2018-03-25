n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
count = 0
for i in arr :
    if i in s1 :
        count = count + 1
    if i in s2 :
        count = count - 1
print(count)
