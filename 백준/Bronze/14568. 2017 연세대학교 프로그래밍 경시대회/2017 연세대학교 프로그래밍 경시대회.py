N = int(input())
a = 0
for i in range(1, N + 1):
    for j in range(i + 2, N + 1 - i):
        for k in range(2, N + 1 - i - j):
            if i + j + k == N and k % 2 == 0:
                a += 1
print(a)