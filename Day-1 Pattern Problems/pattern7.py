num = 5

for row in range(num):
    for space in range(row):
        print(' ',end='')
    for col in range(num-row):
        print('*',end='')
    print()