num = 5

for row in range(num):
    for space in range(num-row -1):
        print(' ',end='')
    for col in range(row+1):
        print('* ',end='')
    print()