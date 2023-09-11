C = int(input())
n = 1
while C != 1:
    if C % 2 == 0:
        C //= 2
    else:
        C = 3 * C + 1
    n += 1
print(n)