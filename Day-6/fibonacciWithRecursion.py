
def fib(num):
    if num == 1: return 0
    elif num == 2: return 1
    else:
        a = 0
        b = 1
        return  fib(num-1) + fib(num-2)
    

print(fib(8))