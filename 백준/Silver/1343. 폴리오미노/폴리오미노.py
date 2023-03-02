a = input()
flag = True
curr = ''
prev = ''
i = 0
count = 0
p = []
while i < len(a):
    curr = a[i]
    if curr == '.':
        if count > 0:
            if count % 2 == 0:
                for _ in range(count // 4):
                    p.append("AAAA")
                for _ in range((count % 4) // 2):
                    p.append("BB")
            else:
                flag = False
                break
        count = 0
    else:
        count += 1
    prev = curr
    i += 1
if curr != '.':
    if count > 0:
        if count % 2 == 0:
            for _ in range(count // 4):
                p.append("AAAA")
            for _ in range((count % 4) // 2):
                p.append("BB")
        else:
            flag = False
i = 0
j = 0
ans = ''
if flag:
    while i < len(a):
        if a[i] == 'X':
            for l in range(len(p[j])):
                ans += p[j][l]
                i += 1
            j += 1
        elif a[i] == '.':
            ans += '.'
            i += 1
else:
    ans = -1
print(ans)