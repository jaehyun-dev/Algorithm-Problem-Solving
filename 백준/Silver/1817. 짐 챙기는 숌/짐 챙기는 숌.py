N, M = map(int, input().split())
if 0 < N:
    b = list(map(int, input().split()))
    cnt = 0
    m = 0
    for i in b:
        if m + i <= M:
            m += i
        else:
            m = i
            cnt += 1
    print(cnt + 1)
else:
    print(0)