N, M, K = map(int, input().split())
mn = max(0, N - M * K)
mx = max(0, N - M * (K - 1) - 1)
print(mn, mx)
