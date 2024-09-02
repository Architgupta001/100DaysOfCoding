num = 5

for row in range(num):
    for space in range(row):
        print(' ',end='')
    for col in range((2*num - 2*row)-1):
        print('*',end='')
    print()