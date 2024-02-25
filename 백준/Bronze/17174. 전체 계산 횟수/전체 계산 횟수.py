N, M = map(int, input().split())
cnt = N
while 0 < N:
    N //= M
    cnt += N
print(cnt)