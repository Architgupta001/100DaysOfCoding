# Method 1

def sumOfList(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum


print('Method 1: ',sumOfList([6,1,2,3]))

# Method 2 using recursion

def sumList(lst):
    if len(lst)==1: return lst[0]
    else:
        return lst[0] + sumList(lst[1:])

print('Method 2: ',sumList([6,1,2,3]))