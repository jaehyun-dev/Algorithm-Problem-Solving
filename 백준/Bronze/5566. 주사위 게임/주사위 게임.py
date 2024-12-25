N, M = map(int, input().split())
X = [0] * N
for n in range(N):
    X[n] = int(input())
cnt = 0
i = 0
while i < N - 1:
    i += int(input())
    if i < N:
        i += X[i]
    cnt += 1
print(cnt)