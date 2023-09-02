a, b, c = sorted(list(map(int, input().split())))
if a + b <= c:
    print((a + b) * 2 - 1)
else:
    print(a + b + c)