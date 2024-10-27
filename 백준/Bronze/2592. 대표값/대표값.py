s = 0
d = {}
for _ in range(10):
    a = int(input())
    s += a
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
f = 0
for i in d:
    if f < d[i]:
        f = d[i]
        m = i
print(s // 10)
print(m)