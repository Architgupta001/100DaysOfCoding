# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    # your code goes here
    vowels = 'aeiouAEIOU'
    stuartScore = 0
    kevinScore = 0
    sizeOfString = len(string)
    
    for i in range(sizeOfString):
        if string[i] in vowels:
            kevinScore += sizeOfString - i
        if string[i] not in vowels:
            stuartScore += sizeOfString - i
    
    if kevinScore>stuartScore:
        print('Kevin', kevinScore)
    elif kevinScore<stuartScore:
        print('Stuart', stuartScore)
    else:
        print('Draw')
    
if __name__ == '__main__':
    s = input()
    minion_game(s)