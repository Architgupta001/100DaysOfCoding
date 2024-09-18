# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    str_lst = list(string)
    str_lst[position] = character
    return "".join(str_lst)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)