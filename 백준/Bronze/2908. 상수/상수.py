a, b = input().split()
c, d = [], []
for i in range(3):
    c.append(a[2 - i])
    d.append(b[2 - i])
e, f = int(c[0] + c[1] + c[2]), int(d[0] + d[1] + d[2])
print(max(e, f))