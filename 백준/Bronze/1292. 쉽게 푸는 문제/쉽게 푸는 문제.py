A, B = map(int, input().split())
ans = 0
i = 1
j = 1
while 1:
    for k in range(j):
        if A <= i <= B:
            ans += j
        i += 1
    j += 1
    if B < i:
        break
print(ans)