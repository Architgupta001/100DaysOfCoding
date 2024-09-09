
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        prod = 1
        for i in range(2,num+1):
            prod = prod * i
        return prod
    
print(fact(4))