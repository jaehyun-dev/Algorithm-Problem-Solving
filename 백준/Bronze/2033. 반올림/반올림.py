N = input()
l = len(N)
n = int(N)
i = 0
while i < l - 1:
    if 5 <= n % 10:
        n += 10 - n % 10
    n //= 10
    i += 1
print(n * (10 ** (l - 1)))