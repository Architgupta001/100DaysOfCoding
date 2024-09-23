# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

import numpy as np

Nrow, Mrow, Pcol = map(int, input().split())
lst = []

for i in range(Nrow+Mrow):
    values = input().split()
    lst.append(values)
    my_array = np.array(lst)

my_array = my_array.astype(int)
print(my_array)

# use concatenation istead of direct read