N = int(input())
a = [False] * max(4, N + 1)
a[1] = True
a[3] = True
for i in range(4, N + 1):
    if a[i - 4]:
        a[i] = True
print("SK" if a[N] else "CY")