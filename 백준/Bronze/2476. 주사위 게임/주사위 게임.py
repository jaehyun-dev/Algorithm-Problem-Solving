N = int(input())
M = 0
for _ in range(N):
    a = sorted(list(map(int, input().split())), reverse=True)
    s = set(a)
    if len(s) == 1:
        p = 10000 + a[0] * 1000
    elif len(s) == 2:
        p = 1000 + a[0] * 100
    else:
        p = a[0] * 100
    M = max(M, p)
print(M)