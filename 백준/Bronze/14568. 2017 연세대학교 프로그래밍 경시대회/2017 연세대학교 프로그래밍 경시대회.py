N = int(input())
a = 0
for i in range(1, N - 4):
    for j in range(i + 2, N - 1 - i):
        if (N - i - j) > 1 and (N - i - j) % 2 == 0:
            a += 1
print(a)