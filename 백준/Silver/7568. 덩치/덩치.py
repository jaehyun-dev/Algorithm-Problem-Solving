n = int(input())
student = []
for _ in range(n):
    x, y = map(int, input().split())
    student.append([x, y])

rank = []
for i in range(n):
    count = 1
    for j in range(n):
        if student[i][0] < student[j][0] and student[i][1] < student[j][1]:
            count += 1
    rank.append(count)

for i in range(n - 1):
    print(rank[i], end=" ")
print(rank[-1])