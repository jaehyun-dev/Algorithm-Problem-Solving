a = input()
l = len(a)
ans = a
for i in range(1, l - 1):
    for j in range(i + 1, l):
        w = a[:i][::-1] + a[i:j][::-1] + a[j:][::-1]
        if w < ans:
            ans = w
print(ans)