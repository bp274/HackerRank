def minion_game(string):
    stuscore = kevscore = 0
    length = len(string)
    for i in range(length) :
        if s[i] in ('A', 'E', 'I', 'O', 'U') :
            kevscore += length - i
        else :
            stuscore += length - i
    print ("Stuart " + str(stuscore) if stuscore > kevscore else "Kevin " + str(kevscore) if kevscore > stuscore else "Draw")
