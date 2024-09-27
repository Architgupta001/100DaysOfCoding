# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

eng_stu = int(input())
eng_set_stu = set(map(int, input().split()))

french_stu = int(input())
french_set_stu = set(map(int, input().split()))

final_set = eng_set_stu.difference(french_set_stu)

print(len(final_set))

