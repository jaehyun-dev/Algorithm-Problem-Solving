import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a = 0
    N = int(input())
    for _ in range(N):
        a += max(list(map(int, input().split())) + [0])
    print(a)