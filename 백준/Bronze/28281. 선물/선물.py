N, X = map(int, input().split())
A = list(map(int, input().split()))
min_sum = float("inf")
for i in range(N - 1):
    min_sum = min(min_sum, A[i] + A[i + 1])
print(min_sum * X)