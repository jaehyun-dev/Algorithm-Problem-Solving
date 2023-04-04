flag = True
min_num = 100
ans = 0
for _ in range(7):
    a = int(input())
    if a % 2 == 1:
        ans += a
        flag = False
        if a < min_num:
            min_num = a
if flag:
    print(-1)
else:
    print(ans)
    print(min_num)