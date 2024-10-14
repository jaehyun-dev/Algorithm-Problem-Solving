l = list(map(int, input().split()))
while 1:
    flag = 1
    for i in range(4):
        if l[i + 1] < l[i]:
            l[i], l[i + 1] = l[i + 1], l[i]
            print(*l)
            flag = 0
    if flag:
        break