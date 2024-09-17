# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

list = []

def insert(pos, value):
    list.insert(pos, value)
def printList():
    print(list)
def remove(value):
    list.remove(value)
def append(value):
    list.append(value)
def sort():
    list.sort()
def pop():
    list.pop()
def reverse():
    list.reverse()
    
# Create a mapping of command names to functions
func_map = {
    "insert": insert,
    "print": printList,
    "remove": remove,
    "append": append,
    "sort": sort,
    "pop": pop,
    "reverse": reverse
}

if __name__ == '__main__':
    N = int(input())
    
    command = []
    for i in range(N):
        user_command = input()
        command.append(user_command)
        
    for j in command:
        a = j.split()
        if len(a) == 3:
            func = func_map.get(a[0])
            func(int(a[1]), int(a[2]))
        elif len(a) == 2:
            func = func_map.get(a[0])
            func(int(a[1]))
        elif len(a) == 1:
            func = func_map.get(a[0])
            func()
        else:
            print('No such function found')
        