# https://www.hackerrank.com/contests/assignment-4/challenges/magic-even-and-odd/problem

num = int(input())
sum = 0

for i in range(num):
    a = int(num%10)
    b = int(num//10)
    num = b
    sum += a

if(sum%2==0):
    print("Magic even")
if(sum%2!=0):
    print("Magic odd")