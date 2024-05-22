K, N = map(int, input().split())
if N == 1:
    print(-1)
else:
    ans = (K * N) // (N - 1)
    if (K * N) % (N - 1):
        ans += 1
    print(ans)