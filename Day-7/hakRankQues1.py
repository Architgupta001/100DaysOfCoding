# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])
sorted_students = sorted(students)
# print(students)
# print(sorted_students)

for j in range(len(sorted_students)):
    if sorted_students[j][0]<sorted_students[j+1][0]:
        sec_lowest = sorted_students[j+1][0]
        break
    else:
        continue
        
for k in range(len(sorted_students)):
    if (sorted_students[k][0] == sec_lowest):
        print(sorted_students[k][1])
        

