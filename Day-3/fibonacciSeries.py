# Fibonacci series upto 10 numbers
num = int(input('Enter a number: '))
if (num == 1):print('1')
a,b = 0,1
print(a,end=' ')
print(b,end=' ')
for i in range(2,num):
    c = a+b
    a,b=b,c
    print(c,end=' ')