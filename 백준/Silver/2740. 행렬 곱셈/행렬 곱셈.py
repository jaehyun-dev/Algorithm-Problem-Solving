N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))
C = [([0] * K) for _ in range(N)]
for i in range(N):
    for j in range(K):
        n = 0
        for k in range(M):
            n += A[i][k] * B[k][j]
        C[i][j] = n
for r in C:
    print(*r)