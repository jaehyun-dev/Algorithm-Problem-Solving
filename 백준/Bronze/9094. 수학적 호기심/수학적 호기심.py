T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    count = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i ** 2 + j ** 2 + m) / (i * j) == (i ** 2 + j ** 2 + m) // (i * j):
                count += 1
    print(count)