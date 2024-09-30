n = int(input())
a = list(map(int, input().split()))
s = sum(a)
a.sort()
cnt = 0
for i in range(n - 1):
    cnt += a[i] * (s - a[i])
    s -= a[i]
print(cnt)