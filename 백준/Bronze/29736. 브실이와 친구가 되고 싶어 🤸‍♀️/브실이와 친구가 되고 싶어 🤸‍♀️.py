A, B = map(int, input().split())
K, X = map(int, input().split())
cnt = 0
for i in range(A, B + 1):
    if abs(K - i) <= X:
        cnt += 1
print(cnt if cnt else "IMPOSSIBLE")