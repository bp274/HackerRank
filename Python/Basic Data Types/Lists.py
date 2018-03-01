if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(0,n):
        commands = input().split()
        if commands[0] == "insert" :
            arr.insert((int(commands[1])),(int(commands[2])))
        elif commands[0] == "append" :
            arr.append(int(commands[1]))
        elif commands[0] == "remove" :
            arr.remove(int(commands[1]))
        elif commands[0] == "reverse" :
            arr.reverse()
        elif commands[0] == "sort" :
            arr.sort()
        elif commands[0] == "pop" :
            arr.pop()
        else :
            print (arr)
