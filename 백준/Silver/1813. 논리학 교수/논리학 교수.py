N = int(input())
I = list(map(int, input().split()))
d = {}
for i in I:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
a = []
for i in d:
    if d[i] == i:
        a.append(i)
if len(a) == 0 and 0 in d:
    print(-1)
else:
    a.sort()
    print(a[-1] if a else 0)