# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true


M = input()
a = set(map(int, input().split()))
N = input()
b = set(map(int, input().split()))
[print(i) for i in sorted(a ^ b)]