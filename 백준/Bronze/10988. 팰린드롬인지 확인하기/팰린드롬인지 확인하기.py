a = input()
ans = 1
for i in range(len(a) // 2):
    if a[i] != a[-(i + 1)]:
        ans = 0
        break
print(ans)