N, K = map(int, input().split())
i = N
cnt = 0
while 1:
    if bin(i)[2:].count('1') <= K:
        break
    i += 1
    cnt += 1
print(cnt)