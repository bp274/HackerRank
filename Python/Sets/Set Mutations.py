_, s = input(), set(map(int, input().split()))
for i in range(int(input())) :
    l = list(input().split())
    s1 = set(map(int, input().split()))
    if l[0] == "intersection_update" :
        s.intersection_update(s1)
    if l[0] == "symmetric_difference_update" :
        s.symmetric_difference_update(s1)
    if l[0] == "difference_update" :
        s.difference_update(s1)
    if l[0] == "update" :
        s.update(s1)
print(sum(s))
