# https://www.hackerrank.com/contests/assignment-4/challenges/pattern-2/problem


num = int(input())

for row in range(1,num+1):
    for spaces in range(num-row+2):
        print(' ',end='')
    for col in range(2*row):
        print('*',end='')
    print()