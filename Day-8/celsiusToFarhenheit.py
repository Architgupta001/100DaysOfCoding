
def cToF(C):
    F = (9/5 * C) + 32
    return F

def fToC(F):
    C = 5/9 * (F - 32) 
    return C

print(cToF(32))
print(fToC(89.6))