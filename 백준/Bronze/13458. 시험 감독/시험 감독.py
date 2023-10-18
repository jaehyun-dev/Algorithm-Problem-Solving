import sys, math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = N
for i in range(N):
    A[i] = max(0, A[i] - B)
    cnt += math.ceil(A[i] / C)
print(cnt)