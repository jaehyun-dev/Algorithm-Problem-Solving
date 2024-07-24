a = input()
b = input()
d_a = {}
d_b = {}
for i in a:
    if i not in d_a:
        d_a[i] = 1
    else:
        d_a[i] += 1
for i in b:
    if i not in d_b:
        d_b[i] = 1
    else:
        d_b[i] += 1
cnt = 0
for i in d_a:
    if i in d_b:
        cnt += abs(d_a[i] - d_b[i])
    else:
        cnt += d_a[i]
for i in d_b:
    if i not in d_a:
        cnt += d_b[i]
print(cnt)