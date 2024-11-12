n = int(input())
f = [1, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    f[i] = (f[i - 2] + f[i - 1] + 1) % 1000000007
print(f[n])