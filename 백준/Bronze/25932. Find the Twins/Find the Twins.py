import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    print(*a)
    b = set(a) & {18, 17}
    if len(b) == 2:
        print("both")
    elif len(b) == 0:
        print("none")
    else:
        if b == {18}:
            print("mack")
        else:
            print("zack")
    print()