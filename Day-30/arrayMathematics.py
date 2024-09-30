# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy

n, m = input().split()

a1 = numpy.array([list(map(int, input().split())) for i in range(int(n))])
a2 = numpy.array([list(map(int, input().split())) for i in range(int(n))])

print(numpy.add(a1, a2))
print(numpy.subtract(a1, a2))
print(numpy.multiply(a1, a2))
print(numpy.floor_divide(a1, a2))
print(numpy.mod(a1, a2))
print(numpy.power(a1, a2))