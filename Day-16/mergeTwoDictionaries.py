dict1 = {'Lisa':99, 'John': '95'}
dict2 = {'Lisa':94, 'Peter': '93'}

# Using bar | operator

print(dict1 | dict2)


# Using ** operator

print({**dict1,**dict2})

# Using copy & update

dict3 = dict2.copy()
dict3.update(dict1)

print(dict3)