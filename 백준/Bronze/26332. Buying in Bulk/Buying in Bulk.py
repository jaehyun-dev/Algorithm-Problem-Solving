n = int(input())
for _ in range(n):
    c, p = map(int, input().split())
    print(c, p)
    print(p * c - (c - 1) * 2)