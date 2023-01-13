a, b = map(int, input().split())
c = (a + b) // 2
d = max(a, b) - c
if c + d == a and max(c, d) - min(c, d) == b:
    print(c, d)
else:
    print(-1)