while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    count = 0
    carry = 0
    while a > 0 or b > 0:
        if (a % 10) + (b % 10) + carry > 9:
            carry = 1
            count += 1
        else:
            carry = 0
        a = a // 10
        b = b // 10
    print(count)