N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))
s = N * (N ** 2 + 1) // 2
flag = 1
for i in range(N):
    if sum(m[i]) != s:
        flag = 0
        break
if flag:
    for i in range(N):
        t = 0
        for j in range(N):
            t += m[j][i]
        if t != s:
            flag = 0
            break
if flag:
    t1 = 0
    t2 = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                t1 += m[i][j]
                t2 += m[i][N - j - 1]
    if t1 != s or t2 != s:
        flag = 0
if flag:
    s1 = set()
    for i in range(N):
        for j in range(N):
            if m[i][j] in s1:
                flag = 0
                break
            else:
                s1.add(m[i][j])
print("TRUE" if flag else "FALSE")