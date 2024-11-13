N = int(input())
ans = 1
while N > 1:
    if N % 2 == 1:
        ans = 0
        break
    N //= 2
print(ans)