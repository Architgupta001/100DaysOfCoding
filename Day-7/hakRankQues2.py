# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math

AB = float(input())
BC = float(input())

radian = math.atan(AB/BC)
degree = math.degrees(radian)

print(f"{round(degree)}\u00B0")