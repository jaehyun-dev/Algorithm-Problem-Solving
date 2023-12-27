N = int(input())
a = []
flag = True
cnt = 0
for _ in range(N):
    D, C = input().split()
    if flag:
        if D != "jinju":
            a.append(int(C))
        else:
            c = int(C)
            for i in a:
                if c < i:
                    cnt += 1
            flag = False
    else:
        if c < int(C):
            cnt += 1
print(c)
print(cnt)