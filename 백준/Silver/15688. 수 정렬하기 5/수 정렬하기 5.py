import sys
input = sys.stdin.readline
N = int(input())
l = [0] * 2000001
for _ in range(N):
    l[int(input()) + 1000000] += 1
for i in range(2000001):
    for j in range(l[i]):
        sys.stdout.write(str(i - 1000000) + "\n")