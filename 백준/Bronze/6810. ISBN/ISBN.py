n = '9780921418'
a, b, c = input(), input(), input()
num = n + a + b + c
ans = 0
for i in range(13):
    if i % 2 == 0:
        ans += int(num[i])
    else:
        ans += int(num[i]) * 3

print(f"The 1-3-sum is {ans}")