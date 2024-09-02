num = 5

for row in range(2*num):
    if row<num:
        for space in range(row):
            print(' ',end='')
        for col in range(num-row):
            print('* ',end='')
    else:
        for space in range(2*num-row-1):
            print(' ',end='')
        for col in range(row - num+1):
            print('* ',end='')     
    print()