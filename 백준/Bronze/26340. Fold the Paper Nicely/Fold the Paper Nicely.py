n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    a1, b1, c1 = a, b, c
    for _ in range(c):
        if a > b:
            a //= 2
        else:
            b //= 2
    ma = max(a, b)
    mi = min(a, b)
    print(f"Data set: {a1} {b1} {c1}")
    print(ma, mi)
    print()