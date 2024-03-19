n = int(input())
if n < 3:
    print(0)
elif n == 3:
    print(1)
else:
    ans = 2
    d = 2
    for i in range(1, n - 3):
        ans += d
        if i % 2 == 0:
            d += 1
    print(ans)