# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true

import numpy as np

rows, columns = map(int, input().split())
lst = []

for row in range(rows):
    inp = input().strip().split()
    lst.append(inp)
    arr = np.array(lst)

arr = arr.astype(int)
print(np.transpose(arr))
print(arr.flatten())



