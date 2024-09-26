# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))
c = int(input())

for i in range(c):
    single_command = input().split()
    if single_command[0] == 'pop':
        s.pop()
    elif single_command[0] == 'remove':
        s.remove(int(single_command[1]))
    elif single_command[0] == 'discard':
        s.discard(int(single_command[1]))
    else:
        print('incorrect command')
        
print(sum(s))
