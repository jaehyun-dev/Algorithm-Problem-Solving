L, R, A = map(int, input().split())
m = min(L, R)
M = max(L, R)
d = M - m
m += min(A, d)
A -= min(A, d)
if M - m > 0:
    print(m * 2)
else:
    print(M * 2 + A - (A % 2))