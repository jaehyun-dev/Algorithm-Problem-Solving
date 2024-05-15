l = list(map(int, input().split()))
ans = 1
for i in l:
    if i % 2 == 1:
        ans *= i
if ans == 1:
    if 1 not in l:
        for i in l:
            ans *= i
print(ans)