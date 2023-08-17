import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())
    pt = d + n * p
    st = n * s
    if pt == st:
        print("does not matter")
    else:
        if pt > st:
            print("do not ", end="")
        print("parallelize")