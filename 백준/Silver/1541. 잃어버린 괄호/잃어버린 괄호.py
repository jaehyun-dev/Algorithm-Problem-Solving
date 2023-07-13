a = input()
num = []
oper = []
res = a[0]
for i in range(1, len(a)):
    if a[i].isdigit():
        res += a[i]
    else:
        num.append(res.lstrip('0'))
        res = ""
        oper.append((a[i], i))
num.append(res.lstrip('0'))

sen = ""
for i in range(len(oper)):
    sen += num[i]
    sen += oper[i][0]
sen += num[-1]

target_idx = []
for i in range(1, len(sen)):
    if sen[i] == '-':
        target_idx.append(i)

ans = 0
for i in range(len(target_idx)):
    if i == 0:
        ans += eval(sen[:target_idx[i]])
        if len(target_idx) > 1:
            ans -= eval(sen[target_idx[i] + 1:target_idx[i + 1]])
    elif 0 < i < len(target_idx) - 1:
        ans -= eval(sen[target_idx[i] + 1:target_idx[i + 1]])
    if i == len(target_idx) - 1:
        ans -= eval(sen[(target_idx[i] + 1):])

if len(target_idx) == 0:
    ans = eval(sen)
print(ans)