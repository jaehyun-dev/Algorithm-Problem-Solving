A, B = map(int, input().split())
N = int(input())
m = abs(A - B)
flag = 0
for _ in range(N):
    f = int(input())
    if abs(B - f) < m:
        m = abs(B - f)
        flag = 1
print(m + flag)