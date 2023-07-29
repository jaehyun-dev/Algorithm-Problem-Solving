import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    a = 0
    b = 0
    for _ in range(N):
        C, G = map(float, input().split())
        a += C * G
        b += C
    print(int(b), format(a / b, ".1f"))