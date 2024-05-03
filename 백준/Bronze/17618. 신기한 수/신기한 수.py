N = int(input())
ans = 0
for n in range(1, N + 1):
    s = 0
    i = n
    while 0 < i:
        s += i % 10
        i //= 10
    if n % s == 0:
        ans += 1
print(ans)