# https://www.hackerrank.com/contests/assignment-4/challenges/pattern-1/problem

num = int(input())

for row in range(1,num+1):
    col_range = num-row+1
    for col in range(col_range):
        print(col_range,end='')
    print()