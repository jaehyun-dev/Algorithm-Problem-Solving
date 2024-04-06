M = int(input())
if M <= 30:
    ans = M / 2
else:
    ans = 15 + (M - 30) * 3 / 2
print(format(ans, ".1f"))