N = int(input())
l = [0] * N
for i in range(N):
    l[i] = int(input())
cnt = 0
for i in range(N - 2, -1, -1):
    d = max((l[i] - l[i + 1] + 1), 0)
    l[i] -= d
    cnt += d
print(cnt)