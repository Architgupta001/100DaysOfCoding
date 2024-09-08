num = 4

if num == 1: 
    print('not prime')
elif num == 2: 
    print('prime')
else:
    for i in range(2,num):
        if num%i==0:
            print('Not prime')
            break;
        else:
            print('prime')
            break;