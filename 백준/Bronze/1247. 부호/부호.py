import sys
input = sys.stdin.readline
for _ in range(3):
    N = int(input())
    ans = 0
    for _ in range(N):
        ans += int(input())
    if ans < 0:
        print("-")
    elif ans > 0:
        print("+")
    else:
        print(0)