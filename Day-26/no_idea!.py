# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

m, n = map(int, input().split())

lst = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for i in range(m):
    if lst[i] in A:
        happiness += 1
    if lst[i] in B:
        happiness -= 1
        
print(happiness)