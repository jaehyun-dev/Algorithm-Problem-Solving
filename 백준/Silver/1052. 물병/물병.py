N, K = map(int, input().split())
cnt = 0
while 1:
    if bin(N)[2:].count('1') <= K:
        break
    N += 1
    cnt += 1
print(cnt)