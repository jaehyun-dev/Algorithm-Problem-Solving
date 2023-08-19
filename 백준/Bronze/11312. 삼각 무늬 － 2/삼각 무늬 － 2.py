import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    a = 0
    for i in range(A // B):
        a += 2 * (i + 1) - 1
    print(a)