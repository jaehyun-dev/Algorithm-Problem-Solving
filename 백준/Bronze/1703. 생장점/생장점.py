import sys
input = sys.stdin.readline

while 1:
    a = list(map(int, input().strip().split()))
    if a == [0]:
        break
    ans = 1
    for _ in range(a[0]):
        s, l = a.pop(1), a.pop(1)
        ans *= s
        ans -= l
    print(ans)