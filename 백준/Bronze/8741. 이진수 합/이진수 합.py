k = int(input())
a = 2 ** k - 1
print(bin((1 + a) * a // 2)[2:])