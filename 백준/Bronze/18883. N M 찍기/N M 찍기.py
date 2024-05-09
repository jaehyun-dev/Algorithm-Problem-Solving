N, M = map(int, input().split())
for i in range(N):
    a = []
    for j in range(1, M + 1):
        a.append(i * M + j)
    print(*a)