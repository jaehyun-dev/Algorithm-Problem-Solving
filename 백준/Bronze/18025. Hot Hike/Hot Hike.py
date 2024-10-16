n = int(input())
l = list(map(int, input().split()))
t = 41
d = -1
for i in range(n - 2):
    m = max(l[i], l[i + 2])
    if m < t:
        t = m
        d = i
print(d + 1, t)