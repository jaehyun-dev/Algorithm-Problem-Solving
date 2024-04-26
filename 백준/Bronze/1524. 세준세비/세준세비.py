import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    input()
    a = []
    N, M = map(int, input().split())
    s = list(map(int, input().split()))
    for i in s:
        a.append((i, 1))
    b = list(map(int, input().split()))
    for i in b:
        a.append((i, 0))
    a.sort()
    print("S" if a[-1][1] else "B")