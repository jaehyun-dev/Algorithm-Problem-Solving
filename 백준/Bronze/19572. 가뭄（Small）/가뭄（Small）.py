d1, d2, d3 = map(int, input().split())
a = (d1 + d2 - d3) / 2
b = (d1 + d3 - d2) / 2
c = (d2 + d3 - d1) / 2
if 0 < a and 0 < b and 0 < c:
    print(1)
    print(a, b, c)
else:
    print(-1)