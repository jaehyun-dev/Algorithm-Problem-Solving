b = []
for _ in range(4):
    b.append(input())
s = input()
for i in range(1, 3):
    for j in range(1, 10):
        flag = 1
        for dr, dc in ((0, 0), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
            r = i + dr
            c = j + dc
            if b[r][c] not in s:
                flag = 0
                break
        if flag:
            break
    if flag:
        break
print(b[i][j])