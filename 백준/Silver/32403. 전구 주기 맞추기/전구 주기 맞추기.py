N, T = map(int, input().split())
a = list(map(int, input().split()))
d = set()
for i in range(1, T // 2 + 2):
    if T % i == 0:
        d.add(i)
        d.add(T // i)
cnt = 0
for i in range(N):
    m = a[i]
    for j in d:
         e = abs(a[i] - j)
         if e < m:
             m = e
    cnt += m
print(cnt)