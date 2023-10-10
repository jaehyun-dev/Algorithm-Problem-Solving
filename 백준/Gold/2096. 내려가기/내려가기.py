import sys
input = sys.stdin.readline
N = int(input())
dp_max = list(map(int, input().split()))
dp_min = list(dp_max)
for _ in range(N - 1):
    a = list(map(int, input().split()))
    dp_max = [max(dp_max[0], dp_max[1]) + a[0], max(dp_max) + a[1], max(dp_max[1], dp_max[2]) + a[2]]
    dp_min = [min(dp_min[0], dp_min[1]) + a[0], min(dp_min) + a[1], min(dp_min[1], dp_min[2]) + a[2]]
print(max(dp_max), min(dp_min))