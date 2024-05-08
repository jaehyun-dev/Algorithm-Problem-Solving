N = int(input())
a = [0] * N
a[0] = 1
a[1] = 2
for i in range(2, N - 1):
    a[i] = i + 1
a[N - 1] = 997
print(N)
print(*a)