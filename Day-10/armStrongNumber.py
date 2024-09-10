
number = 9474

len_of_number = len(str(number))
str_number = str(number)

sum = 0

for digit in str_number:
    sum = sum + (int(digit)**len_of_number)

if sum == number:
    print('Armstrong number')
else:
    print('Not an Armstrong number')
