num = 10

def sumOfNaturalNumbers(num):
    if num <= 1:
        return num
    sum = num + sumOfNaturalNumbers(num - 1)
    return sum

print(sumOfNaturalNumbers(num))