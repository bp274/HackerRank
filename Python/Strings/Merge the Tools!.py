def merge_the_tools(string, k):
    new = []
    x = 0
    for i in string :
        x += 1
        if i not in new :
            new.append(i)
        if x == k :
            x = 0
            print("".join(new))
            new = []
