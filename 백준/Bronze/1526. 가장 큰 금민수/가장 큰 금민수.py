N = int(input())
for i in range(N, 0, -1):
    flag = 1
    for j in str(i):
        if j not in ('4', '7'):
            flag = 0
            break
    if flag:
        print(i)
        break