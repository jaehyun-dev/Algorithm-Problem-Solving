import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(N):
    if a[i] != i + 1:
        c += 1
print(c)