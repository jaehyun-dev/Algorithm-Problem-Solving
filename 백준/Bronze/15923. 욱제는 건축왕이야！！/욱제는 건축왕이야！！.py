N = int(input())
l = 0
a0, b0 = map(int, input().split())
a, b = a0, b0
for _ in range(N - 1):
    c, d = map(int, input().split())
    l += abs(a - c) + abs(b - d)
    a, b = c, d
l += abs(a - a0) + abs(b - b0)
print(l)