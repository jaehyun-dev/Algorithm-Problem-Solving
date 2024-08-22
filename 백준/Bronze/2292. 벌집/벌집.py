n = int(input())
if n == 1:
    print(1)
else:
    sum = 1
    count = 1
    i = 1
    while sum < n:
        sum += 6 * i
        i += 1
        count += 1
    print(count)