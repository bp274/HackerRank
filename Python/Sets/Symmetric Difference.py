a = int(input())
set1 = set(map(int, input().split()))
b = int(input())
set2 = set(map(int, input().split()))
l = sorted((set1.union(set2)).difference(set1.intersection(set2)))
for i in l :
    print(i)
