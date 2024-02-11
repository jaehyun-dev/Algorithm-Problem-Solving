a = input()
v = set(['a', 'e', 'i', 'o', 'u'])
cnt = 0
y = 0
for i in a:
    if i in v:
        cnt += 1
    if i == 'y':
        y += 1
print(cnt, cnt + y)