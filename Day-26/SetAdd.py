# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

size = int(input())
countries = set()
for i in range(size):
    country = input()
    countries.add(country)

print(len(countries))