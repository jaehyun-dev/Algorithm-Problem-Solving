import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
V = 0
for i in range(N):
    Ai = A[i]
    V = (1 - (1 - (V / 100)) * (1 - (Ai / 100))) * 100
    print(V)