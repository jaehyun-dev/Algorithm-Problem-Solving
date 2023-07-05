f, a = map(int, input().split())
n = int(input())
for _ in range(n):
    c = int(input())
    print(c, min(c, 1000) * f + max(0, c - 1000) * a)