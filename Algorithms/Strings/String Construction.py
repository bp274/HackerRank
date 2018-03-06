def stringConstruction(s):
    p = ""
    cost = 0
    for i in range(len(s)):
        if s[i] not in p:
            cost = cost + 1
            p = p + s[i]
    return cost

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
