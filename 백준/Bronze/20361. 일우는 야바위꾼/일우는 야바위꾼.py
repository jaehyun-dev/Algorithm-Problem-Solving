N, X, K = map(int, input().split())
ans = X
for _ in range(K):
    A, B = map(int, input().split())
    if A == ans:
        ans = B
    elif B == ans:
        ans = A
print(ans)