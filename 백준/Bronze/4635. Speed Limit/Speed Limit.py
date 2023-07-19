import sys
input = sys.stdin.readline
while 1:
    n = int(input())
    if n == -1:
        break
    d = 0
    p = 0
    for _ in range(n):
        s, t = map(int, input().split())
        d += s * (t - p)
        p = t
    print(f"{d} miles")