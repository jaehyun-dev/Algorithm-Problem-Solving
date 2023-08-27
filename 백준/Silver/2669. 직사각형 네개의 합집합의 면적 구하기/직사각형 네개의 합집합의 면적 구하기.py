a = list()
for _ in range(4):
    a.append(tuple(map(int, input().split())))
b = 0
for i in range(4):
    b += (a[i][2] - a[i][0]) * (a[i][3] - a[i][1])
for i in range(3):
    for j in range(i + 1, 4):
        b -= (max(0, min(a[i][2], a[j][2]) - max(a[i][0], a[j][0]))) * (max(0, min(a[i][3], a[j][3]) - max(a[i][1], a[j][1])))
for i in range(2):
    for j in range(i + 1, 3):
        for k in range(j + 1, 4):
            b += (max(0, min(a[i][2], a[j][2], a[k][2]) - max(a[i][0], a[j][0], a[k][0]))) * (max(0, min(a[i][3], a[j][3], a[k][3]) - max(a[i][1], a[j][1], a[k][1])))
b -= (max(0, min(a[0][2], a[1][2], a[2][2], a[3][2]) - max(a[0][0], a[1][0], a[2][0], a[3][0]))) * (
    max(0, min(a[0][3], a[1][3], a[2][3], a[3][3]) - max(a[0][1], a[1][1], a[2][1], a[3][1])))
print(b)