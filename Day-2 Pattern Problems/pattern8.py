num = 7

for row in range(num):
    for space in range(num-row):
        print(' ',end='')
    for col in range(2*row + 1):
        print('*',end='')
    print()