N, Q = map(int, input().split())
b = [1] * N
for _ in range(Q):
    L, I = map(int, input().split())
    for i in range(L - 1, N, I):
        b[i] = 0
print(sum(b))