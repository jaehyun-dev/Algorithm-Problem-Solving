import sys
input = sys.stdin.readline
while 1:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break
    A = int(B ** (1 / N))
    print(A if abs(A ** N - B) < abs((A + 1) ** N - B) else A + 1)