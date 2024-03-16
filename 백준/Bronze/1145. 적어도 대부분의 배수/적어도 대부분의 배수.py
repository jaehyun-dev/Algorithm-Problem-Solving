a = list(map(int, input().split()))
a.sort()
b = a[2]
while 1:
    cnt = 0
    for n in a:
        if b % n == 0:
            cnt += 1
    if 2 < cnt:
        break
    b += 1
print(b)