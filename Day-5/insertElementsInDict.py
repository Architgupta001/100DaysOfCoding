# Write a script to print a dict where the keys are numbers between 1 and 15 and values are square of keys

dict = {}

# Method 1
for i in range(1,16):
    dict.update({i:i*i})

print(dict)

# Method 2
for i in range(1,16):
    dict[i] = i**2

print(dict)

