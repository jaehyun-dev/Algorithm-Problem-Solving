N, L = map(int, input().split())
a = []
for _ in range(N):
    l = input()
    cnt = 0
    flag = True
    i = 0
    while i < L:
        if l[i] == "1":
            if flag:
                cnt += 1
                flag = False
        else:
            flag = True
        i += 1
    a.append(cnt)
M = max(a)
print(M, a.count(M))