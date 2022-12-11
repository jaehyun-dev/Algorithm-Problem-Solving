import math
m, n = map(int, input().split())
if m < 2:
    check = [True] + [False] * (n - m)
else:
    check = [False] * (n - m + 1)

i = 2
while i <= math.floor(math.sqrt(n)):
    j = max(2, m // i)
    while i * j <= n:
        check_num = i * j
        if check_num >= m and not check[check_num - m]:
            check[check_num - m] = True
        j += 1
    i += 1

for i in range(len(check)):
    if not check[i]:
        print(i + m)