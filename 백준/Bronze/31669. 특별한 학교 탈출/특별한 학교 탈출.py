N, M = map(int, input().split())
graph = [([0] * N) for _ in range(M)]
for i in range(N):
    a = input()
    for j in range(M):
        graph[j][i] = a[j]
for j in range(M):
    flag = 1
    for i in range(N):
        if graph[j][i] == 'O':
            flag = 0
            break
    if flag:
        ans = j + 1
        break
print(ans if flag else "ESCAPE FAILED")