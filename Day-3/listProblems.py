a = ['Ross', 'Rachel', 'Monica', 'Joe']
b = [13,7,12,10] 

# swap first and fourth element

a[0],a[3]=a[3],a[0]
print(a)

# add new value at 2nd position

a.insert(1,"Archit")
print(a)

# delete a value from 3rd position

a.pop(2)
print(a)

# multiply all the number in list

result = 1
for i in b:
    result = result * i
print('Result is ',result)

# largest from the list

b.sort()
print('Largest is ',b[-1])

#smallest from the list

print('Smallest is ',b[0])