import sys
input = sys.stdin.readline
while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    c = []
    c.append(a // b)
    c.append(a - c[0] * b)
    c.append('/')
    c.append(b)
    print(*c)