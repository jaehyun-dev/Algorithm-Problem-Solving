import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    k, l, r = map(int, input().split())
    if k == 1:
        for idx in range(l - 1, r):
            a[idx] = a[idx] ** 2 % 2010
    else:
        print(sum(a[l - 1:r]))