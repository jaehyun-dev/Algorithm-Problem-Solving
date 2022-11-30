a, b = input().split()
c, d = [], []
for i in range(3):
    c.append(a[2 - i])
    d.append(b[2 - i])
e, f = int(c[0] + c[1] + c[2]), int(d[0] + d[1] + d[2])
print(max(e, f))

# habadjen의 답
n1, n2 = input().split()
n1, n2 = int(n1[::-1]), int(n2[::-1])
if n1 > n2:
    print(n1)
else:
    print(n2)
