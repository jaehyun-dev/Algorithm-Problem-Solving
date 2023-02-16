x, y = map(int, input().split())
a = 100 - x
b = 100 - y
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
print(a, b, c, d, q, r)
if d // 100 == 0:
    print(c, d)
else:
    print(c + q, r)