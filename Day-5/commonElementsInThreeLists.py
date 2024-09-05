a = [1,5,6,3,4]
b = [5,1,2,4,5,9,3,5]
c = [1,3,4]

# method 1
a,b,c = set(a),set(b),set(c)

x = a.intersection(b)
y = x.intersection(c)

print("Common elements in three lists are ",y)

# method 2

print("Common elements in three lists are ",set(a) & set(b) & set(c))