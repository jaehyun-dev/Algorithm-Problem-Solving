N, D, p = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range(N):
    while 0 < A[i]:
        A[i] -= D
        cnt += 1
    if i == N - 1:
        break
    if A[i] < 0:
        A[i + 1] = max(0, A[i + 1] - (-A[i] * p // 100))
print(cnt)