# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    new = numpy.array(arr)
    new = new.astype(float)
    rev = new[: :-1]
    return rev

arr = input().strip().split(' ')
result = arrays(arr)
print(result)