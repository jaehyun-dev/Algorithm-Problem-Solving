import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    q, r = A, B
    while r:
        q, r = r, q % r
    print(A * B // q)