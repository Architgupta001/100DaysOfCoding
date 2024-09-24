# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

if __name__ == '__main__':
    s = input()
    
check = [False]*5
for i in s:
    if i.isalnum():
        check[0] = True
    if i.isalpha():
        check[1] = True
    if i.isdigit():
        check[2] = True
    if i.islower():
        check[3] = True
    if i.isupper():
        check[4] = True    

[print(x) for x in check]