# method 1 
"""
num = input("Enter any number: ")
rev_num = int(num[::-1])
num = int(num)

if num == rev_num:
    print(num," is palindrome.")
else:
    print(num," is not a palindrome")
"""

# method 2
num2 = int(input("Enter any number: "))
temp = num2
rev = 0

while(num2>0):
    a = num2%10
    b = num2//10
    num2 = b
    rev = rev*10 + a

if temp == rev:
    print(temp," is palindrome.")
else:
    print(temp," is not a palindrome")