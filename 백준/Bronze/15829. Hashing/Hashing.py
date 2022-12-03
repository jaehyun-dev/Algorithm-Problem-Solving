n = int(input())
arr = list(input())
R = 31
M = 1234567891
ans = 0

for i in range(n):
    ans += (ord(arr[i]) - 96) * (R ** i)

print(ans % M)