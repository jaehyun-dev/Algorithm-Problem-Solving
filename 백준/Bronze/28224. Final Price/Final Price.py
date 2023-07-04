import sys
input = sys.stdin.readline
n = int(input())
p = int(input())
for _ in range(n - 1):
    p += int(input())
print(p)