N, K = map(int, input().split())
l = list(map(int, input().split(',')))
for _ in range(K):
    t = [0] * (N - 1)
    for i in range(N - 1):
        t[i] = l[i + 1] - l[i]
    l = t
    N -= 1
print(','.join(map(str, l)))