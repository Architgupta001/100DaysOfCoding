# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true


N, M = map(int, input().split())
for i in range(1, N, 2):
    print((".|." * i).center(M, '-'))

print("WELCOME".center(M, "-"))

for s in range(N-2, 0, -2):
    print((".|."*s).center(M, "-"))