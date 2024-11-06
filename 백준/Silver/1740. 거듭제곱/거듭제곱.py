N = int(input())
n = int(bin(N)[2:])
ans = 0
i = 0
while 0 < n:
    ans += (n % 10) * (3 ** i)
    n //= 10
    i += 1
print(ans)