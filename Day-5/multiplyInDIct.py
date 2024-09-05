# multiply all the items in dict

dict = {'a':14,'b':24,'c':36,'d':34,'e':15}

result = 1

for i in dict:
    value = dict[i]
    result = result * value

print(result)