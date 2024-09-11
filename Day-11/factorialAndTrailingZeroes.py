

def factorial(user_input):
    if user_input == 0 or user_input == 1: 
        return 1
    else:
        factUsingRecursion = user_input * factorial(user_input - 1)
        return factUsingRecursion
    
def trailingZeroes(Factorial):
    # Factorial = str(Factorial)
    count = 0
    if Factorial == 0: return 0 
    while(Factorial%10 == 0):
        count += 1
        Factorial//= 10
    return count


if __name__ == '__main__':
    user_input = int(input('Enter any number: '))
    Factorial = factorial(user_input)
    print(f'Factorial of {user_input} is {Factorial}')
    print(f'Number of trailing zeroes in {Factorial} is {trailingZeroes(Factorial)}')
