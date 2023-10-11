N, M, P = map(int, input().split())
outer_flag = False
flag = True
for _ in range(N):
    s = list(map(int, input().split()))
    s.sort()
    cnt = s.count(-1)
    l = s[cnt:]
    for i in l:
        if i <= P:
            P += i
        else:
            if cnt > 0:
                P *= 2
                cnt -= 1
                if i <= P:
                    P += i
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    for i in range(cnt):
        P *= 2
    if not flag:
        break
print(1 if flag else 0)