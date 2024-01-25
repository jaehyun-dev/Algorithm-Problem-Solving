import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = list(input().split())
flag = 0
ans = []
for i in range(N - 1):
    for j in range(i + 1, N):
        if abs(X[i] - X[j]) <= L[i] + L[j] and C[i] != C[j]:
            ans = [i + 1, j + 1]
            flag = 1
            break
    if flag:
        break
if flag:
    print("YES")
    print(*ans)
else:
    print("NO")