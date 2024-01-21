N, K, P = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
cnt = 0
for n in range(N):
    for k in range(K):
        if b[n * K + k] == 0:
            cnt += 1
    if cnt < P:
        ans += 1
print(ans)