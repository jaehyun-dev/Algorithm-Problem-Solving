N = int(input())
cnt = 0
for i in range(2, N - 1):
    cnt += (i - 1) * (N - i - 1)
print(cnt * N // 4)