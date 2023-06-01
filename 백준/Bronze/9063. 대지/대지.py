import sys
input = sys.stdin.readline
n = int(input())
left = 10000
right = -10000
upper = -10000
lower = 10000
for _ in range(n):
    a = list(map(int, input().split()))
    left = min(left, a[0])
    right = max(right, a[0])
    upper = max(upper, a[1])
    lower = min(lower, a[1])
print((right - left) * (upper - lower))