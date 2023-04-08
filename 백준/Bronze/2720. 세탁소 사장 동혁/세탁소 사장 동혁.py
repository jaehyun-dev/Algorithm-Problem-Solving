T = int(input())
for _ in range(T):
    a = int(input())
    q = a // 25
    a %= 25
    d = a // 10
    a %= 10
    n = a // 5
    a %= 5
    p = a
    print(q, d, n, p)