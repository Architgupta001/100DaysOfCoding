# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        lis=[]
        for m in range(i, i+k):
            if string[m] not in lis:
                lis.append(string[m])
        print("".join(lis))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)