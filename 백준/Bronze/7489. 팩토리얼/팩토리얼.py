t = int(input())
for _ in range(t):
    n = int(input())
    ans = 1
    i = 1
    while i <= n:
        ans *= i
        cnt_2 = 0
        cnt_5 = 0
        temp = ans
        while temp % 2 == 0:
            temp //= 2
            cnt_2 += 1
        while temp % 5 == 0:
            temp //= 5
            cnt_5 += 1
        for j in range(min(cnt_2, cnt_5)):
            ans //= 10
            cnt_2 -= 1
            cnt_5 -= 1
        if cnt_2 == 0 and cnt_5 == 0:
            ans %= 10
        i += 1
    if ans % 10:
        ans %= 10
    print(ans)