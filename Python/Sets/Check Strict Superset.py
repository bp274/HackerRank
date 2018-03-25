s = set(input().split())
for i in range(int(input())) :
    s1 = set(input().split())
    if s.intersection(s1) != s1 or len(s) <= len(s1) :
        print("False")
        exit(1)
print("True")
