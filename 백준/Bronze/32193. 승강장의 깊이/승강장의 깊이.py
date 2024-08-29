import sys
input = sys.stdin.readline
N = int(input())
a = b = 0
for _ in range(N):
    A, B = map(int, input().split())
    a += A
    b += B
    print(a - b)