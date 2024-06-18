a, b, c = map(int, input().split())
if not a:
    print(c ** 2 - b)
elif not b:
    print(c ** 2 - a)
else:
    print(int((a + b) ** (1 / 2)))