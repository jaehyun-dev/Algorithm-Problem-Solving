N = int(input())
l = [[], [], []]
for _ in range(N):
    a = list(map(int, input().split()))
    for i in range(3):
        l[i].append(a[i])
s = [0] * N
for i in range(N):
    for j in range(3):
        if l[j].count(l[j][i]) == 1:
            s[i] += l[j][i]
for i in range(N):
    print(s[i])