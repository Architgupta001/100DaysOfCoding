
divisor = 13
divisible = 100

# using for loop

for i in range(1,divisible):
    if i%divisor == 0:
        print(i,end=' ')

# using lambda and filter()

lst = [13, 14, 2, 6 , 26 , 39 , 52 , 65 , 78 , 91 , 23, 11, 22]

result = list(filter(lambda x: x % divisor == 0,lst))
print()
print(result,end=' ')
