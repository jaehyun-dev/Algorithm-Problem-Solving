N, K = map(int, input().split())
A = list(map(int, input().split()))
for a in A:
    N -= (a + 1) // 2
print("NO" if N > 0 else "YES")