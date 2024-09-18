# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    new_str = ""
    for letter in s:
        if letter.islower():
            new_str += letter.upper()
        elif letter.isupper():
            new_str += letter.lower()
        else:
            new_str += letter
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)