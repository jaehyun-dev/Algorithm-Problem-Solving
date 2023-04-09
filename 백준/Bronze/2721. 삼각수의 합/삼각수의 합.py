T = int(input())
for _ in range(T):
    n = int(input())
    num = 0
    for k in range(1, n + 1):
        num += k * (k + 1) * (k + 2) // 2
    print(num)