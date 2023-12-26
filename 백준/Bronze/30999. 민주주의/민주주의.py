N, M = map(int, input().split())
cnt = 0
for _ in range(N):
    a = input()
    o = 0
    x = 0
    for i in range(M):
        if a[i] == "O":
            o += 1
        else:
            x += 1
        if M // 2 < o:
            cnt += 1
            break
        if M // 2 < x:
            break
print(cnt)