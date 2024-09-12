a = 20
b = 35

def highestCommonFactor(x,y):
    if x>y: smallest = y
    else: smallest = x

    for i in range(1,smallest + 1):
        if(x%i == 0) and (y%i == 0):
            HCF = i
    return HCF

print(highestCommonFactor(a,b))