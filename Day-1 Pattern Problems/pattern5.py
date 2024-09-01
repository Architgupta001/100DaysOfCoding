num = 5

for row in range(1,2*num):
    if(row<num):
        for col in range(row):
            print('*',end=' ')
    else:
        for col in range(2*num - row):
            print('*', end=" ")
    print()