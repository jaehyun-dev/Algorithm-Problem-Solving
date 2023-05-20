import sys
input = sys.stdin.readline
while 1:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    print(A * 2 - B)