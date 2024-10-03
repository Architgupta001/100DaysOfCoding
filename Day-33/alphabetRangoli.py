# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def make_line(number_of_letters, size):
    x = 97 + size - number_of_letters
    line = ""
    for i in range(number_of_letters -1, -1, -1):
        line += chr(x+i) + "-"
    for i in range(1, number_of_letters):
        line += chr(x+i) + "-"
    return line[:-1]

def print_rangoli(size):
    m= ((size*2)-1) + (size-1) * 2
    for i in range(1, size+1):
        pattern = make_line(i, size)
        print(pattern.center(m, "-"))
    for j in range(size -1, 0, -1):
        pattern2 = make_line(j, size)
        print(pattern2.center(m, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)