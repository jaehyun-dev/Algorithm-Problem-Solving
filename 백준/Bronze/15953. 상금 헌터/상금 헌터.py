c1 = [0] * 101
p1 = [500, 300, 200, 50, 30, 10]
c2 = [0] * 101
p2 = [512, 256, 128, 64, 32]
i = 1
j = 0
idx = 1
flag = 0
while 1:
    for _ in range(i):
        if 21 < idx:
            flag = 1
            break
        c1[idx] = p1[j]
        idx += 1
    if flag:
        break
    i += 1
    j += 1
i = 0
j = 0
idx = 1
flag = 0
while 1:
    for _ in range(2 ** i):
        if 31 < idx:
            flag = 1
            break
        c2[idx] = p2[j]
        idx += 1
    if flag:
        break
    i += 1
    j += 1

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print((c1[a] + c2[b]) * 10000)