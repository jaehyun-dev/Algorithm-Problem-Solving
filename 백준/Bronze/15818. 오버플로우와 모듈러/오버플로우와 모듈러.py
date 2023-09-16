N, M = map(int, input().split())
a = list(map(int, input().split()))
c = 1
for i in range(N):
    c = (c * (a[i] % M)) % M
print(c)