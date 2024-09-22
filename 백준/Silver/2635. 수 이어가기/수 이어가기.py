N = int(input())
M = 0
ans = []
for i in range(N // 2, N * 2 // 3 + 2):
    a, b = N, i
    temp = [a, b]
    cnt = 1
    while 0 <= b:
        a, b = b, a - b
        temp.append(b)
        cnt += 1
    if M < cnt:
        M = cnt
        ans = temp
print(M)
print(*ans[:-1])