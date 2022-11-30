min_num, max_num = map(int, input().split())
check = [False] * (max_num - min_num + 1)

i = 2
while i ** 2 <= max_num:
    j = min_num // (i ** 2)
    while i ** 2 * j <= max_num:
        check_num = i ** 2 * j
        if check_num >= min_num and not check[check_num - min_num]:
            check[check_num - min_num] = True
        j += 1
    i += 1

print(check.count(False))