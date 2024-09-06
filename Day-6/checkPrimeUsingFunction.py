
def primeOrNot(num):
    if num == 1:
        print(num,' is not prime.')
    if num == 2:
        print(num,' is prime.')
    else: 
        for i in range(2,num):
            if num%i == 0:
                print(num,' is not prime.')
                break;
            else:
                print(num,' is prime.')
                break;


primeOrNot(23)