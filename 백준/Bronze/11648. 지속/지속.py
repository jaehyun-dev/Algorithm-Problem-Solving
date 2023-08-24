n = input()
cnt = 0
while 1:
    if len(n) == 1:
        break
    num = 1
    for i in range(len(n)):
        num *= int(n[i])
    cnt += 1
    n = str(num)
print(cnt)