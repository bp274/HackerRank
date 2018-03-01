if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    while 1 :
        if(arr[n-1] == arr[n-2]):
            arr.pop()
            n = n - 1
        else :
            break
    print(arr[n-2])
    
