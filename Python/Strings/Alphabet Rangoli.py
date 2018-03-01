def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size - 1, -size, -1) :
        print("-".join(alphabets[size - 1 : abs(i) : -1] + (alphabets[abs(i) : size])).center(4*size - 3, "-"))
