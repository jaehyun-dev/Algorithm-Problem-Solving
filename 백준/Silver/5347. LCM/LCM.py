n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    q, r = a, b
    while r:
        q, r = r, q % r
    print(a * b // q)