a = [1,2,3,4,5,6,7,8,9,10]

def evenFromList(a):
    b = []
    for i in range(len(a)):
        if a[i]%2 == 0:
            b.append(a[i])
    return b

print(a)
print(evenFromList(a))
