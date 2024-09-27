# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

len_of_A = int(input())
A = set(map(int, input().split()))
no_of_other_sets = int(input())

for i in range(no_of_other_sets):
    command = input().split()
    B = set(map(int, input().split()))
    
    if command[0] == 'intersection_update':
        A.intersection_update(B)
    elif command[0] == 'update':
        A.update(B)
    elif command[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif command[0] == 'difference_update':
        A.difference_update(B)
    else:
        print('wrong command')

print(sum(A))



