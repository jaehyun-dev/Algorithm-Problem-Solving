import sys
input = sys.stdin.readline
while 1:
    s, d, v = map(int, input().split())
    if (s, d, v) == (0, 0, 0):
        break
    if (v - s) % d == 0:
        a = (v - s) // d
        if a >= 0:
            print(a + 1)
        else:
            print("X")
    else:
        print("X")