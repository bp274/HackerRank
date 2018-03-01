if __name__ == '__main__':
    result = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        result.append([score, name])
    result.sort()
    result.reverse()
    m = n - 1
    k = result.pop()
    for i in range(n-1) :
        if result[m-1-i][0] == k[0] :
            result.pop()
            m = m - 1
    k = result.pop()
    print(k[1])
    n = m - 1
    for i in range(m-1) :
        if result[n-1-i][0] == k[0] :
            print(result.pop()[1])
            result.pop()
            n = n - 1
