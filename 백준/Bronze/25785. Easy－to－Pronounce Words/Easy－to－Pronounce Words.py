a = input()
p = a[0]
i = 1
flag = 1
v = ['a', 'e', 'i', 'o', 'u']
while i < len(a):
    c = a[i]
    if p in v:
        if c not in v:
            i += 1
        else:
            flag = 0
            break
    else:
        if c in v:
            i += 1
        else:
            flag = 0
            break
    p = c
print(flag)