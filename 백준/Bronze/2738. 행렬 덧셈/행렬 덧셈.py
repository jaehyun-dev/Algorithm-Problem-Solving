N, M = map(int, input().split())
A = []
B = []

ans = []
for i in range(N):
    ans.append([])
    for j in range(M):
        ans[i].append(0)

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        ans[i][j] = A[i][j] + B[i][j]

for i in range(N):
    for j in range(M):
        print(ans[i][j], end=" ")
    print()