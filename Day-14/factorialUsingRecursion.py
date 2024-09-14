num = 3

def fact(num):
    if num<=0:
        return "Doesn't exist"
    elif num == 1:
        return 1
    else:
        return num * fact(num-1)
    
print(fact(num))