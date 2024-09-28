# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter

k = int(input())
lst = list(map(int, input().split()))
st = set(lst)
room_count = Counter(lst)

for i in st:
    if room_count[i]<k:
        print(i)
