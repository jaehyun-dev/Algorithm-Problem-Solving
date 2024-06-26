N = int(input())
d = {}
for _ in range(N):
    a = input()[0]
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
l = []
for a in d:
    if 4 < d[a]:
        l.append(a)
if len(l):
    l.sort()
    for a in l:
        print(a, end="")
else:
    print("PREDAJA")