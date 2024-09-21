# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy as np

user_input = input().strip().split()
lst = []
for i in user_input:
    lst.append(i)

array = np.array([lst[0:3], lst[3:6], lst[6:9]])

print(array.astype(int))

 

