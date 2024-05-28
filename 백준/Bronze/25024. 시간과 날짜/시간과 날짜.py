import sys
input = sys.stdin.readline

c = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    if 0 <= x < 24 and 0 <= y < 60:
        t = "Yes"
    else:
        t = "No"
    if 1 <= x < 13 and 1 <= y <= c[x]:
        d = "Yes"
    else:
        d = "No"
    print(t, d)